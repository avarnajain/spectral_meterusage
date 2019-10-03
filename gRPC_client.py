import grpc

# import the generated classes
import meterValue_pb2
import meterValue_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = meterValue_pb2_grpc.meterUsageValuesStub(channel)

# create a valid request message
request = meterValue_pb2.Date(date_str='2019-01-02')

# make the call
response = stub.getMeterData(request)

# et voilà
print(response.value)