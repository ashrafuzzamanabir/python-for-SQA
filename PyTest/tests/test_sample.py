# content of test_sample.py
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