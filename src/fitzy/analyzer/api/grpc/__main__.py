import logging

from fitzy.analyzer.api.grpc.server import server

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    server.add_insecure_port("[::]:6790")
    server.start()
    server.wait_for_termination()
