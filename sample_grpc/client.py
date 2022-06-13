import grpc 
import sample_pb2
import sample_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = sample_pb2_grpc.RouteGuideStub(channel)

    feature = stub.GetFeature(sample_pb2.Point(latitude=409146138, longitude=-746188906))
    print(feature)