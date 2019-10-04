import grpc

# import the generated classes
import meterValue_pb2
import meterValue_pb2_grpc

def create_gRPC_request(date_start, date_end):
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    # create a stub (client)
    stub = meterValue_pb2_grpc.meterUsageValuesStub(channel)
    # create a valid request message
    request = meterValue_pb2.Dates(date_start=date_start, date_end=date_end)
    # make the call
    response = stub.getMeterData(request)
    print('gRPC client returning response')
    # print response
    return response.values