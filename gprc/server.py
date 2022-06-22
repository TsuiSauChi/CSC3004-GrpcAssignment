import grpc
from concurrent import futures
from datetime import datetime

import tracking_pb2
import tracking_pb2_grpc

# Test Connection
import psycopg2 as pg

# Database Connection Config
### NEED TO REFCATOR HERE ###
# conn = pg.connect(
#     host="174.138.23.75",
#     database="testing",
#     user="postgres",
#     password="cl0udplus!"
# )

conn = pg.connect(
    host="localhost",
    database="grpc",
    user="jamestsui",
    password="password"
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
    def Login(self, request, context):
        cur.execute("""
        SELECT r.rolename, u.name FROM Users u 
            INNER JOIN Roles r 
                ON u.role_id = r.id
            WHERE u.name = %s and u.nric = %s;
        """, (request.name, request.nric))
        result = cur.fetchone()

        if result is not None:
            # Set User Session
            currentuser = result[1]
            print(currentuser + " is logged in")
            return tracking_pb2.User(
                name=currentuser, 
                role_name=result[0], 
                status = tracking_pb2.Status(status=True))
        else:
            return tracking_pb2.User(
                status = tracking_pb2.Status(status=True)
            )

    # Get All Locations 
    def GetAllLocations(self, request, context):
        cur.execute("SELECT name FROM locations")
        result = cur.fetchall()
        for row in result:
            yield tracking_pb2.Location(
                name = row[0]
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
    def CreateGroup(self, request, context):
        print("Request", request)
        cur.execute("SELECT name FROM Groups WHERE name = %s", (request.name,))
        existing_group = cur.fetchone()
        if existing_group is not None:
            print("Group name already exist")
            return tracking_pb2.Group(status= tracking_pb2.Status(status=False))
        else:
            cur.execute("INSERT INTO Groups (name) VALUES (%s) returning id;", (request.name,))
            group_id = cur.fetchone()[0]
            conn.commit()
            # Add currentuser into new group
            try:
                cur.execute("""
                INSERT INTO UserGroups (user_id, group_id) VALUES (
                    (SELECT id FROM Users WHERE name = %s),
                    %s
                )
                """, (currentuser, group_id))
                print("Testing", group_id, currentuser)
                conn.commit()
                return tracking_pb2.Group(
                        name = request.name,
                        status= tracking_pb2.Status(status=True)
                    )
            except Exception as e:
                print("Create Group Error")
                print(e)
                return tracking_pb2.Group(status=tracking_pb2.Status(status=False))

    # Add User to Group
    # Condition: What if no user exist?
    def AddUserToGroup(self, request_iterator, context):
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
    def CreateCheckInIndividual(self, request, context):
        print("Check in Individual Request", request)
        try:
            cur.execute("""
                        INSERT INTO Checkinouts (user_id, location_id)
                        VALUES (
                            (SELECT id FROM Users WHERE name = %s),
                            (SELECT id FROM Locations WHERE name = %s)
                        );
                        """, (currentuser, request.name))
            conn.commit()
            return tracking_pb2.Status(status=True)
        except Exception as e:
            print("Check in Individual Error")
            print(e)
            return tracking_pb2.Status(status=False)

    # Create Check In For Group
    def CreateCheckInGroup(self, request, context):
        try:
            print("Check in Individual Request", request)
            cur.execute("""
                INSERT INTO Checkinouts (user_id, group_id, location_id)
                            VALUES (
                                (SELECT id FROM Users WHERE name = %s),
                                (SELECT id FROM Groups WHERE name = %s),
                                (SELECT id FROM Locations WHERE name = %s)
                );
            """, (currentuser, request.group.name , request.name))
            conn.commit()
            return tracking_pb2.Status(status=True)
        except Exception as e:
            print("Check in Individual Error")
            print(e)
            return tracking_pb2.Status(status=False)

    # Get All possible Check-out options
    def GetCheckOutOptions(self, request, context):
        cur.execute("""
            SELECT c.id, g.name, l.name from Checkinouts c 
                INNER JOIN Locations l 
                    ON l.id = c.location_id
                INNER JOIN Users u 
                    ON c.user_id = u.id 
                LEFT JOIN Groups g 
                    ON c.group_id = g.id
            WHERE c.check_out IS NULL;
        """)
        result = cur.fetchall()
        for row in result:
            yield tracking_pb2.CheckOut(
                id = row[0],
                location = tracking_pb2.Location(
                    name = row[2]
                ),
                group = tracking_pb2.Group(
                    name = row[1]
                )
            )

    # Create Check Out For Individual 
    def CreateCheckOut(self, request, context):
        try:
            cur.execute("""
            UPDATE Checkinouts c
            SET check_out = CURRENT_TIMESTAMP
            WHERE c.id = %s
            """, (request.id,))
            conn.commit()
            return tracking_pb2.Status(status=True)
        except Exception as e:
            print("Check out Individual Error")
            print(e)
            return tracking_pb2.Status(status=False)

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