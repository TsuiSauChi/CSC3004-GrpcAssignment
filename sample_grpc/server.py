from email import message

from concurrent import futures
import grpc
import sample_pb2
import sample_pb2_grpc

# What is this
class SampleService(sample_pb2_grpc.RouteGuideServicer):
    
    def GetFeature(self, request, context):
        return sample_pb2.Feature(message='Hello, %s!' % request.latitude)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_RouteGuideServicer_to_server(SampleService(), server)
    # What is this?
    server.add_insecure_port('[::]:50051')
    server.start()
    # Block calling thread until server terminates
    server.wait_for_termination()

serve()