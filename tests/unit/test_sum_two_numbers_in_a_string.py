from operators.sum_two_numbers_in_a_string import sum_two_numbers_in_a_string
import pytest

@pytest.mark.parametrize("input, target", [("1,2", 3), ("2,2", 4), ("-1,-2", -3)])
def test_sum_two_numbers_in_a_string(input, target):
    result = sum_two_numbers_in_a_string(input)
    assert result == target