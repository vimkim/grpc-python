import grpc
from concurrent import futures
import time

# Import the generated classes
import hello_pb2
import hello_pb2_grpc

# Implement the Greeter service
class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message=f'Hello, {request.name}!')

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    # Listen on port 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

