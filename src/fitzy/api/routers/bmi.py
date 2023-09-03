from fastapi import APIRouter

from fitzy.core import analyze_bmi, calculate_bmi

router = APIRouter(prefix="/bmi")


@router.get("/analyze")
def analyze(weight: float, height: float) -> str:
    """
    Calculate and analyze the BMI based on the weight (kg) and height (cm).
    """
    calculated_bmi = calculate_bmi(weight_in_kg=weight, height_in_cm=height)
    bmi_analyzation_result = analyze_bmi(calculated_bmi)
    return bmi_analyzation_result.value
