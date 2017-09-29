
from concurrent import futures
import grpc

import web_graph_pb2 as pb2
import web_graph_pb2_grpc as gpb2

class WebGraphBuilder(gpb2.WebGraphServicer):
    """Dummy web graph builder server"""

    def AddEdge(self, request, context):
        print(request)
        return pb2.Result(status=0)

def main():
    print("OPA")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    gpb2.add_WebGraphServicer_to_server(WebGraphBuilder(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    while True:
        # grpc is not blocking
        pass

if __name__ == "__main__":
    main()
