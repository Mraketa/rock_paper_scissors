import pytest
from fz import fizzbuzz

# testy by na sobe mely byt nezavisle

def test_fizzbuzz_takes_number_returns_str():
    result = fizzbuzz(1)
    assert isinstance(result, str)
    
@pytest.mark.parametrize('number', [1,2,4,7])
    
def test_fizzbuzz_1_returns_1():
    result = fizzbuzz(1)
    assert result == '1'

def test_fizzbuzz_2_returns_2():
    result = fizzbuzz(2)
    assert result == '2'

def test_fizzbuzz_3_returns_fizz():
    result = fizzbuzz(3)
    assert result == 'fizz'

def test_fizzbuzz_5_returns_buzz():
    result = fizzbuzz(5)
    assert result == 'buzz'