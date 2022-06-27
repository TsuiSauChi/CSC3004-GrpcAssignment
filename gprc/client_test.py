import grpc
from concurrent import futures
from datetime import datetime

import tracking_pb2
import tracking_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = tracking_pb2_grpc.TrackingServiceStub(channel)

a = datetime.now()
stub.LatencyTest(tracking_pb2.Time(time = str(a)))
b = datetime.now()

print(b-a)
