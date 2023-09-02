
def test_addition():
    assert add(2, 3) == 5

def test_negative_numbers():
    assert add(-2, 3) == 1

def test_decimal_numbers():
    assert add(1.5, 2.5) == 4.0
