from email import message
from scipy.fftpack import fftn
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
currentuser = None

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
    def CreateCheckOutIndividual(self, request, context):
        return super().CreateCheckOutIndividual(request, context)

    # Create Check In For Group
    # Condition: Check whether currentuser belongs to the group
    # Condition: What if user check-in to the same location?
    # Condition: What if there is double check-in without check-out;
        # Error showing the previous check-in?
    # Condition: What if there is no current user; back to login?
    # Condition: Need is a query to get all the groups for the current user
    def CheckInGroup(self, request, context):
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


    # Get Safe Entry Details By User; Need Get Location Info
    def GetSafeEntry(self, request, context):
        print("Running query")
        cur.execute("""SELECT * from Checkinouts c
                    INNER JOIN Users u
                        ON c.user_id = u.id
                    WHERE u.id = (
                        SELECT id from Users 
                            WHERE name = %s
                    );""", (request.name,))

        result = cur.fetchall()
        for row in result:
            yield tracking_pb2.CheckIn(
                checkin = row[3].strftime("%m/%d/%Y, %H:%M:%S"), 
                checkout = row[4].strftime("%m/%d/%Y, %H:%M:%S")
            )
        

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tracking_pb2_grpc.add_TrackingServiceServicer_to_server(
        TrackingService(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

serve()