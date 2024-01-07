import grpc

from fitzy.analyzer.api.grpc.services.bmi_pb2 import (
    BmiServiceAnalyzeRequest,
    BmiServiceAnalyzeResponse,
)
from fitzy.analyzer.api.grpc.services.bmi_pb2_grpc import (
    BmiServiceServicer as BmiServiceServicerInterface,
)
from fitzy.analyzer.core import analyze_bmi, calculate_bmi


class BmiServiceServicer(BmiServiceServicerInterface):
    def Analyze(
        self,
        request: BmiServiceAnalyzeRequest,
        context: grpc.ServicerContext,
    ) -> BmiServiceAnalyzeResponse:
        calculated_bmi = calculate_bmi(
            weight_in_kg=request.weight, height_in_cm=request.height
        )
        bmi_analyzation_result = analyze_bmi(calculated_bmi)
        return BmiServiceAnalyzeResponse(result=bmi_analyzation_result.value)
