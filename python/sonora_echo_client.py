import echo_pb2_grpc
import echo_pb2
import sonora.client


with sonora.client.insecure_web_channel(
    f"http://192.168.3.1:8080"
) as channel:
    er = echo_pb2.EchoRequest()
    er.message = "hello"
    stub = echo_pb2_grpc.EchoServiceStub(channel)    
    print(stub.Echo(er))

    
