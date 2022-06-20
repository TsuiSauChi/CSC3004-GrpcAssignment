import grpc
from concurrent import futures
from datetime import datetime

import tracking_pb2
import tracking_pb2_grpc

# Test Connection
import psycopg2 as pg

# Database Connection Config
### NEED TO REFCATOR HERE ###
conn = pg.connect(
    host="174.138.23.75",
    database="testing",
    user="postgres",
    password="cl0udplus!"
)

cur =  conn.cursor()

# Set currentuser
#currentuser = None
currentuser = 'user1'

# Notify contract tracking cases for the past 14 days
def notifyUser(case_id):
    cur.execute("""
        SELECT DISTINCT u.name FROM Users u 
        INNER JOIN Checkinouts c 
            ON u.id = c.user_id
        WHERE c.check_in::DATE - 14 <= (
            SELECT date FROM Cases WHERE id = %s
        );
    """, case_id)
    result = cur.fetchall()

    # Logic: Send telegram notification to all user

class TrackingService(tracking_pb2_grpc.TrackingServiceServicer):
    
    # Condition: What if user does not exist; upsert into the database
    # Condition: Need to check roll
    def Login(self, request, context):
          cur.execute("SELECT name, nric FROM users WHERE name = %s AND nric = %s", 
            (request.name, request.nric))
          result = cur.fetchone()

          print(result)

          if result is not None:
              currentuser = result[0]
              print(currentuser + " is logged in")
              return tracking_pb2.Status(message="T")
          return tracking_pb2.Status(message="T")

    # Get User Role
    def GetUserRole(self, request, context):
        cur.execute("""
            SELECT r.rolename FROM Roles r 
            INNER JOIN Users u 
                ON u.role_id = r.id 
            WHERE u.name = 'user1';
        """, (currentuser,))
        result = cur.fetchone()
        return tracking_pb2.Role(rolename = result)

    # Get All Locations 
    def GetAllLocations(self, request, context):
        cur.execute("SELECT name FROM locations")
        result = cur.fetchall()
        for row in result:
            yield tracking_pb2.Location(
                location = row[0]
            )

    # Get All groups by current User
    def GetGroupsByUser(self, request, context):
        cur.execute("""
        SELECT g.name FROM Groups g
            INNER JOIN UserGroups ug 
                ON ug.group_id = g.id 
            INNER JOIN Users u  
                ON ug.user_id = u.id 
            WHERE u.name = %s;
        """, (currentuser,))
        result = cur.fetchall()
        for row in result:
            yield tracking_pb2.Group(
                name = row[0]
            )

    # Create New Group 
    # Need to test here
    def CreateGroup(self, request, context):
        # Create new group
        print("Running", request)
        cur.execute("INSERT INTO Groups (name) VALUES (%s) returning id;", (request.name,))
        group_id = cur.fetchone()[0]
        # Add currentuser into new group
        try:
            cur.execute("""
            INSERT INTO UserGroups (user_id, group_id) VALUES (
                (SELECT id FROM Users WHERE name = %s),
                %s
            )
            """, (currentuser, group_id))
            return tracking_pb2.Status(message="T")
        except Exception as e:
            print("Create Group Error")
            print(e)
            return tracking_pb2.Status(message="F")

    # Add User to Group
    # Condition: What if no user exist?
    def AddUserToGroup(self, request_iterator, context):
        print("running request", request_iterator)
        try:
            for user in request_iterator:
                print(user)
                cur.execute("""
                INSERT INTO UserGroups (user_id, group_id) VALUES (
                    (SELECT id FROM Users WHERE name = %s),
                    (SELECT id FROM Groups WHERE name = %s)
                )
                """, (user.name, user.group.name))
            conn.commit()
            return tracking_pb2.Status(message="T")
        except Exception as e:
            print("Add User To Group Error")
            print(e)
            return tracking_pb2.Status(message="F")
        
   
    # Create Check In For Individual 
    # Condition: What if user check-in to the same location?
    # Condition: What if there is double check-in without check-out
    # Condition: What if there is no current user; back to login?
    def CheckInIndividual(self, request, context):
        try:
            cur.execute("""
                        INSERT INTO Checkinouts (user_id, location_id)
                        VALUES (
                            (SELECT id FROM Users WHERE name = %s),
                            (SELECT id FROM Locations WHERE name = %s)
                        );
                        """, (request.user.name, request.location))
            conn.commit()
            return tracking_pb2.Status(message="T")
        except Exception as e:
            print("Check in Individual Error")
            print(e)
            return tracking_pb2.Status(message="F")

    # Create Check Out For Individual 
    # Condition: What if user the check-in is several days ago?
    # Condition: Check out exist already; is it a postgresql issue
    # Condition: What if user did not check out?
    def CreateCheckOutIndividual(self, request, context):
        try:
            cur.execute("""
            UPDATE Checkinouts c
            SET check_out = CURRENT_TIMESTAMP
            WHERE c.id = (
                SELECT c.id FROM Checkinouts c
                    INNER JOIN Users u
                        ON c.user_id = u.id 
                    INNER JOIN Locations l 
                        ON c.location_id = l.id
                    WHERE u.name = %s AND l.name = %s
                    ORDER BY c.check_in DESC
                LIMIT 1
            );
            """, (currentuser, request.location))
            conn.commit()
            return tracking_pb2.Status(message="T")
        except Exception as e:
            print("Check out Individual Error")
            print(e)
            return tracking_pb2.Status(message="F")

    # Create Check In For Group
    # Condition: Check whether currentuser belongs to the group
    # Condition: What if user check-in to the same location?
    # Condition: What if there is double check-in without check-out;
        # Error showing the previous check-in?
    # Condition: What if there is no current user; back to login?
    # Condition: Need is a query to get all the groups for the current user
    def CreateCheckInGroup(self, request, context):
        print(request)
        try:
            cur.execute("""
                        SELECT DISTINCT u.name FROM Users u
                        INNER JOIN UserGroups ug 
                            ON u.id = ug.user_id 
                        INNER JOIN Groups g 
                            ON g.id = ug.group_id 
                        WHERE g.id = (
                            SELECT id FROM Groups 
                                WHERE name = %s 
                        );
                        """, (request.name))
            users = cur.fetchall()
            for row in users:
                cur.execute("""
                        INSERT INTO Checkinouts (user_id, location_id)
                            VALUES (
                                (SELECT id FROM Users WHERE name = %s),
                                (SELECT id FROM Locations WHERE name = %s)
                            );
                            """, (row[0], request.location))
            conn.commit()
            return tracking_pb2.Status(message="T")
        except Exception as e:
            print("Check in Group Error")
            print(e)
            return tracking_pb2.Status(message="F")

    # Create Check out For Group
    # Condition: What if user the check-in is several days ago?
    # Condition: Check out exist already; is it a postgresql issue
    # Condition: What if user did not check out?
    def CreateCheckOutGroup(self, request, context):
        try:
            cur.execute("""
                            SELECT DISTINCT u.name FROM Users u
                            INNER JOIN UserGroups ug 
                                ON u.id = ug.user_id 
                            INNER JOIN Groups g 
                                ON g.id = ug.group_id 
                            WHERE g.id = (
                                SELECT id FROM Groups 
                                    WHERE name = 'group1'
                            );
                            """, (request.name))
            users = cur.fetchall()
            print(users)
            for row in users:
                cur.execute("""
                UPDATE Checkinouts c
                SET check_out = CURRENT_TIMESTAMP
                WHERE c.id = (
                    SELECT c.id FROM Checkinouts c
                        INNER JOIN Users u
                            ON c.user_id = u.id 
                        INNER JOIN Locations l 
                            ON c.location_id = l.id
                        WHERE u.name = %s AND l.name = %s
                        ORDER BY c.check_in DESC
                    LIMIT 1
                );
                """, (row[0], request.location))
            conn.commit()
            return tracking_pb2.Status(message="T")
        except Exception as e:
            print("Check out Group Error")
            print(e)
            return tracking_pb2.Status(message="F")

    # Get Safe Entry Details By User; Need Get Location Info
    def GetSafeEntry(self, request, context):
        cur.execute("""SELECT * from Checkinouts c
                    INNER JOIN Users u
                        ON c.user_id = u.id
                    WHERE u.id = (
                        SELECT id from Users 
                            WHERE name = %s
                    );""", (currentuser))

        result = cur.fetchall()
        for row in result:
            yield tracking_pb2.CheckIn(
                checkin = row[3].strftime("%m/%d/%Y, %H:%M:%S"), 
                checkout = row[4].strftime("%m/%d/%Y, %H:%M:%S")
            )

    # Create a Covid Case
    # Condition: Error Tracking
    def CreateReportCovidCase(self, request, context):
        cur.execute("""
            INSERT INTO Cases (user_id, location_id) VALUES (
                (SELECT id FROM Users WHERE name = %s),
                (SELECT id FROM Locations WHERE name = %s)
            ) returning id;
        """, (request.user.name, request.location.location))
        case_id = cur.fetchone()[0]
        notifyUser(case_id)
        
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tracking_pb2_grpc.add_TrackingServiceServicer_to_server(
        TrackingService(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

serve()