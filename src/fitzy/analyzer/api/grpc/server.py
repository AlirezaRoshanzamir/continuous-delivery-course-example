from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

from fitzy.analyzer.api.grpc.services import bmi_pb2, bmi_pb2_grpc
from fitzy.analyzer.api.grpc.services.bmi import BmiServiceServicer

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
bmi_pb2_grpc.add_BmiServiceServicer_to_server(BmiServiceServicer(), server)

SERVICE_NAMES = (
    bmi_pb2.DESCRIPTOR.services_by_name["BmiService"].full_name,
    reflection.SERVICE_NAME,
)
reflection.enable_server_reflection(SERVICE_NAMES, server)
