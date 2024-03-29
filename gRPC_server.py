import grpc
from concurrent import futures
import time

# import the generated classes
import meterValue_pb2
import meterValue_pb2_grpc

# import the original grpc_functions.py
import grpc_functions

# create a class to define the server grpc_functions, derived from
# meterValue_pb2_grpc.meterUsageValuesServicer
class meterUsageValuesServicer(meterValue_pb2_grpc.meterUsageValuesServicer):

    def getMeterData(self, request, context):
        print('Request Made to gRPC server')
        # initialize response object
        response = meterValue_pb2.dateValues()
        # store grpc_functions.get_data return as values
        response.values = grpc_functions.get_data(request.date_start, request.date_end)
        # return response
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_meterUsageValuesServicer_to_server`
# to add the defined class to the server
meterValue_pb2_grpc.add_meterUsageValuesServicer_to_server(
        meterUsageValuesServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)