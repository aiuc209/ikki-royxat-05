import pytest

def calculate_total_weight(numbers, weights):
    return sum(num * weight for num, weight in zip(numbers, weights))

def test_calculate_total_weight():
    numbers = [1, 2, 3]
    weights = [2, 3, 4]
    assert calculate_total_weight(numbers, weights) == 1*2 + 2*3 + 3*4

def test_calculate_total_weight_empty_lists():
    numbers = []
    weights = []
    assert calculate_total_weight(numbers, weights) == 0

def test_calculate_total_weight_different_length_lists():
    numbers = [1, 2, 3]
    weights = [2, 3]
    with pytest.raises(ValueError):
        calculate_total_weight(numbers, weights)

def test_calculate_total_weight_negative_numbers():
    numbers = [-1, 2, 3]
    weights = [2, 3, 4]
    assert calculate_total_weight(numbers, weights) == -1*2 + 2*3 + 3*4

def test_calculate_total_weight_negative_weights():
    numbers = [1, 2, 3]
    weights = [-2, 3, 4]
    assert calculate_total_weight(numbers, weights) == 1*-2 + 2*3 + 3*4
