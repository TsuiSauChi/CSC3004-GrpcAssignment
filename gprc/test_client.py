import grpc
from concurrent import futures

import tracking_pb2
import tracking_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = tracking_pb2_grpc.TrackingServiceStub(channel)

result = stub.CreateCheckOutGroup(tracking_pb2.CheckInGroup(
    name = "group1",
    location = "Orchard Road"
))
print(result)

