import grpc
from concurrent import futures

import tracking_pb2
import tracking_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = tracking_pb2_grpc.TrackingServiceStub(channel)

successCheckInGroup = stub.CreateCheckInGroup(tracking_pb2.CheckInGroup(
    name="group1",
    location="Orchard Road")
)
print(successCheckInGroup)


# def handler():
#     for i in range(2,5):
#         yield tracking_pb2.User(name='user'+str(i), group =tracking_pb2.Group(name='group2'))

# stub.AddUserToGroup(handler())

