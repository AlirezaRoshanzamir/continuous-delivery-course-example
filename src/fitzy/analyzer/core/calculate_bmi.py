def calculate_bmi(height_in_cm: float, weight_in_kg: float) -> float:
    """
    Calculate the BMI based on the height and weight.

    Example::

        >>> calculate_bmi(150, 56.25)
        25.0
        >>> calculate_bmi(175, 56.25)
        18.367346938775512

    :param height_in_cm: The height (cm) to be used for the BMI calculation.
    :param weight_in_kg: The weight (kg) to be used for the BMI calculation.
    :returns: The calculated value.
    """
    if height_in_cm <= 0:
        raise ValueError("Height cannot be zero or negative.")

    if weight_in_kg <= 0:
        raise ValueError("Weight cannot be zero or negative.")

    return weight_in_kg / ((height_in_cm / 100) ** 2)
