from pytest import raises

from fitzy.analyzer.core import calculate_bmi


def test_negative_height_should_raise_error() -> None:
    # Arrange
    negative_height = -1
    dummy_weight = 10

    # Act, Assert
    with raises(ValueError):
        calculate_bmi(negative_height, dummy_weight)
