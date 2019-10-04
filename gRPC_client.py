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

# make the call
response = stub.getMeterData(request)

# print response
print(response.values)