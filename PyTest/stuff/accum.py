import pytest
class Accumulator:
    def __init__(self) -> None:
        """
        Initializes a new instance of the Accumulator class.

        This constructor sets the initial value of the private attribute `_count` to 0.

        Parameters:
            None

        Returns:
            None
        """
        self._count = 0

    @property
    def count(self) -> int:
        """
        Returns the value of the private attribute `_count` of the `Accumulator` object.
        
        :return: An integer representing the current count.
        :rtype: int
        """
        return self._count
    
    def add(self, more = 1) -> None:
        """
        Adds the specified number to the current count of the Accumulator object.

        :param more: An optional integer representing the number to be added to the count. Default is 1.
        :type more: int
        :return: None
        """
        self._count += more

    
    