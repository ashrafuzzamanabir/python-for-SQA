import pytest

from stuff.accum import Accumulator

def test_accumulator_init():
    """
    Test the initialization of the Accumulator class.

    This function creates an instance of the Accumulator class and asserts that the initial value of the count property is 0.

    Parameters:
    - None

    Returns:
    - None
    """
    acc = Accumulator()
    assert acc.count == 0

def test_accumulator_add():
    """
    Test the add method of the Accumulator class.

    This function creates an instance of the Accumulator class and calls the add method. It then asserts that the count property of the Accumulator instance is equal to 1.

    Parameters:
    - None

    Returns:
    - None
    """
    acc = Accumulator()
    acc.add()
    assert acc.count == 1

def test_accumulator_add_three():
    """
    Test the add method of the Accumulator class with a value of 3.

    This function creates an instance of the Accumulator class and calls the add method with a value of 3. It then asserts that the count property of the Accumulator instance is equal to 3.

    Parameters:
    - None

    Returns:
    - None
    """
    acc = Accumulator()
    acc.add(3)
    assert acc.count == 3

def test_accumulator_add_tWICE():
    """
    Test the add method of the Accumulator class by calling it twice and asserting that the count property is equal to 2.

    This function creates an instance of the Accumulator class and calls the add method twice. It then asserts that the count property of the Accumulator instance is equal to 2.

    Parameters:
    - None

    Returns:
    - None
    """
    acc = Accumulator()
    acc.add()
    acc.add()
    assert acc.count == 2

def test_accumulator_cannot_set_count_directly():
    """
    Test that the Accumulator object cannot set the count property directly.

    This function creates an instance of the Accumulator class and attempts to set the count property directly. It uses the pytest.raises
    context manager to assert that an AttributeError is raised with the message "property count or accumulator object has no setter".

    Parameters:
    - None

    Returns:
    - None
    """
    acc = Accumulator()
    with pytest.raises(AttributeError,match="property count or accumulator object  has no setter"):
        assert acc.count ==1













