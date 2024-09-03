import grpc

# Import the generated classes
import hello_pb2
import hello_pb2_grpc

def run():
    # Create a channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = hello_pb2_grpc.GreeterStub(channel)

        # Create a request message
        request = hello_pb2.HelloRequest(name='World')

        # Make the call
        response = stub.SayHello(request)
        print("Client received: " + response.message)

if __name__ == '__main__':
    run()

