from operators.string_to_number import string_to_int as s2i

def sum_two_numbers_in_a_string(input: str) -> int:
    numbers_as_string = input.split(',')
    assert len(numbers_as_string) == 2, 'should be 2 numbers'
    numbers = [s2i(item) for item in numbers_as_string]
    return sum(numbers)