from __future__ import annotations

from enum import Enum


def analyze_bmi(bmi_value: float) -> BmiAnalyziationResult:
    if bmi_value <= 0:
        raise ValueError("BMI value cannot be zero or negative.")

    if bmi_value <= 18.4:
        return BmiAnalyziationResult.UNDERWEIGHT
    elif bmi_value <= 24.9:
        return BmiAnalyziationResult.HEALTHY
    elif bmi_value <= 29.9:
        return BmiAnalyziationResult.OVERWEIGHT
    elif bmi_value <= 34.9:
        return BmiAnalyziationResult.OBESITY_CLASS1
    elif bmi_value <= 39.9:
        return BmiAnalyziationResult.OBESITY_CLASS2
    else:
        return BmiAnalyziationResult.OBESITY_CLASS3


class BmiAnalyziationResult(str, Enum):
    UNDERWEIGHT = "UNDERWEIGHT"
    HEALTHY = "HEALTHY"
    OVERWEIGHT = "OVERWEIGHT"
    OBESITY_CLASS1 = "OBESITY_CLASS1"
    OBESITY_CLASS2 = "OBESITY_CLASS2"
    OBESITY_CLASS3 = "OBESITY_CLASS3"
