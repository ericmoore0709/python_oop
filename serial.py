"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Initializes the generator with a starting int value."
        self.start = start
        self.value = start

    def generate(self) -> int:
        "Increments the counter and returns the pre-incremented value, giving a 'generated' serial value."
        self.value += 1
        return self.value - 1
    
    def reset(self) -> None:
        "Resets the counter value to the start value."
        self.value = self.start
    
    def __repr__(self) -> str:
        return f"SerialGenerator(start={self.start}, value={self.value})"