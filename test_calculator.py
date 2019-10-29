from calculator import add, multiply
import pytest

def test_add_two_numbers():
    assert add(0, 0)== 0

def test_add_two_negative_numbers():
    assert add(-55, -2)== -57

def test_add_one_negative_one_positive_number():
    assert add(-4, 9)== 5

def test_add_many_numbers():
    assert add(1, 2, 3,4,5,6,7)== 28

def test_multiply_two_numbers():
    assert multiply(5, 5) == 25

def test_multiply_two_negative_numbers():
    assert multiply(-8, -5) == 40

def test_multiply_many_numbers():
    assert multiply(4, 5, 6, 2, 10) == 2400

def test_add_string_int():
    with pytest.raises(TypeError):
        add('Funny how it fails', 22)

def multiply_string_with_number():
    with pytest.raises(TypeError) as err:
        multiply('MOON', 2)
    assert 'TypeError' in str(err.value)

