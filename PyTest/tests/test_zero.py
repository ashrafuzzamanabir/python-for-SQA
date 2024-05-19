# content of test_sample.py
import pytest
def test_one_plus_one():
    """
        Test the equality of the sum of 1 and 1 with 2.

        This function does not take any parameters and does not return anything.
        It raises an AssertionError if the sum of 1 and 1 is not equal to 2.
    """
    assert 1+1==2

def test_one_plus_two():
    """
    Test the equality of the sum of 2 and 1 with 3.

    This function does not take any parameters and does not return anything.
    It raises an AssertionError if the sum of 2 and 1 is not equal to 3.
    """
    a=2
    b=1
    c=3
    assert a+b==c


def test_devided_by_zero():
    """
    Test if dividing 1 by 0 raises a ZeroDivisionError and if the error message contains the phrase "division by zero".
    
    This function does not take any parameters and does not return anything.
    It raises an AssertionError if the division by zero does not raise a ZeroDivisionError or if the error message does not contain the phrase "division by zero".
    """
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    
    assert "division by zero" in str(e.value)

def test_recursion_depth():
    """
    Test the maximum recursion depth exceeded error by attempting to recursively call the function 'f' until the maximum depth is reached.
    
    This function does not take any parameters and does not return anything.
    It raises an AssertionError if the error message does not contain the phrase "maximum recursion depth exceeded".
    """
    with pytest.raises(RuntimeError) as e:

        def f():
            f()

        f()
    
    assert "maximum recursion depth exceeded" in str(e.value)

    

