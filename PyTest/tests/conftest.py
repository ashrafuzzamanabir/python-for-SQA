import pytest

from stuff.accum import Accumulator


@pytest.fixture
def accum():
    return Accumulator()

@pytest.fixture
def accum2():
    return Accumulator()


@pytest.fixture
def accum3():
    """
    A fixture that returns an instance of the Accumulator class.

    This fixture is used to create an instance of the Accumulator class and make it available for use in test functions. The fixture is decorated with the `@pytest.fixture` decorator, indicating that it is a fixture function.

    Returns:
        Accumulator: An instance of the Accumulator class.

    Yields:
        Accumulator: An instance of the Accumulator class.

    """
    yield Accumulator() #geneareter
    print("done with the test!") #cleanup test


@pytest.fixture
def accum4(scope="session"):
    """
    A fixture that returns an instance of the Accumulator class.

    This fixture is used to create an instance of the Accumulator class and make it available for use in test functions. The fixture is decorated with the `@pytest.fixture` decorator, indicating that it is a fixture function.

    Parameters:
        scope (str, optional): The scope of the fixture. Defaults to "session".

    Yields:
        Accumulator: An instance of the Accumulator class.

    """
    yield Accumulator()
    print("done with the test!")