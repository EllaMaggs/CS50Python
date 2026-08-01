## Use python -m pytest calculator_test.py to run the tests
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(4) == 16

def test_negative():
    assert square(-1) == 1
    assert square(-3) == 9

def main():
    test_square()

if __name__ == "__main__":
    main()