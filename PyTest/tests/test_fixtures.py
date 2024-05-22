import pytest
# from stuff.accum import Accumulator


# @pytest.fixture
# def accum():
    # """
    # A fixture that returns an instance of the Accumulator class.

    # This fixture is used to create an instance of the Accumulator class and make it available for use in test functions. The fixture is decorated with the `@pytest.fixture` decorator, indicating that it is a fixture function.

    # Returns:
    #     Accumulator: An instance of the Accumulator class.

    # """
    # return Accumulator()

def test_accumulator_init(accum):
    """
    Test the initialization of the Accumulator class.

    This function creates an instance of the Accumulator class and asserts that the initial value of the count property is 0.

    Args:
        accum (Accumulator): An instance of the Accumulator class.

    Returns:
        None
    """
    assert accum.count == 0

def test_accumulator_add_one(accum):
    """
    Test the `add` method of the `accum` object by adding one and asserting that the `count` property is equal to 1.

    Parameters:
        accum (Accumulator): The accumulator object to be tested.

    Returns:
        None
    """
    accum.add()
    assert accum.count ==1

def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count ==3

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count ==2

def test_accumulator_cannot_set_count_directly(accum):
    """
    Test that the Accumulator object cannot set the count property directly.

    This function creates an instance of the Accumulator class and attempts to set the count property directly. It uses the pytest.raises
    context manager to assert that an AttributeError is raised with the message "property count or accumulator object has no setter".

    Parameters:
    - accum (Accumulator): The accumulator object to be tested.

    Returns:
    - None
    """
    with pytest.raises(AttributeError,match="property count or accumulator object has no setter"):
        accum.count = 10