import grpc

# import the generated classes
import meterValue_pb2
import meterValue_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = meterValue_pb2_grpc.meterUsageValuesStub(channel)

# create a valid request message
request = meterValue_pb2.Dates(date_start='2019-01-02', date_end='2019-01-03')
# print('request', request, type(request))
# print('request date', request.date_str, type(request.date_str))
# make the call
response = stub.getMeterData(request)
# et voilà
print(response)