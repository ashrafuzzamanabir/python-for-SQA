# multiplication test ideas:
# two positive integers
#identify : multiply by 1
# zero : multiply by 0
# positive by negetive
# negetive by negetive
# float

import pytest


products = [
    (1, 2, 2),
    (2, 99, 99),
    (0, 99, 0),
    (0, -2, 0),
    (2, -10, 20),
    (-2, -1, 2),
    (1.8, 1.2, 2.56)
]

"""
        Test the multiplication of two numbers and verify that the result is equal to the expected product.

        Parameters:
            a (int or float): The first number to be multiplied.
            b (int or float): The second number to be multiplied.
            product (int or float): The expected product of the multiplication.

        Raises:
            AssertionError: If the actual product is not equal to the expected product.
"""

"""
    Test the multiplication of two numbers using parameterized tests.

    This function takes in three parameters: `a`, `b`, and `product`.
    It uses the `pytest.mark.parametrize` decorator to run the test multiple times with different values for `a`, `b`, and `product`.
    The test asserts that the product of `a` and `b` is equal to the expected `product`.

    Parameters:
        a (int): The first number to be multiplied.
        b (int): The second number to be multiplied.
        product (int): The expected product of `a` and `b`.

    Returns:
        None
    """
@pytest.mark.parametrize("a,b,product", products)
def test_multiplication(a,b,product):
    assert a*b == product
