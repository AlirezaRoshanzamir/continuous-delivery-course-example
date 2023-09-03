def calculate_bmi(height_in_cm: float, weight_in_kg: float) -> float:
    if height_in_cm <= 0:
        raise ValueError("Height cannot be zero or negative.")

    if weight_in_kg <= 0:
        raise ValueError("Weight cannot be zero or negative.")

    return weight_in_kg / ((height_in_cm / 100) ** 2)
