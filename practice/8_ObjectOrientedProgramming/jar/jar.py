"""
(Written by: Jeff Truesdell 2025-12-27)
"""


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        new_size = self.size + n

        if 0 <= new_size <= self.capacity:
            self.size = new_size
            return
        else:
            raise ValueError("Error: Invalid Deposit")

    def withdraw(self, n):
        new_size = self.size - n

        if 0 <= new_size <= self.capacity:
            self.size = new_size
            return
        else:
            raise ValueError("Error: Invalid withdraw")

    # Getter
    @property
    def capacity(self):
        return self._capacity

    # Setter
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != int:
            raise ValueError("Capacity is wrong type.")
        if capacity < 0:
            raise ValueError("Capacity must be greater than zero")
        self._capacity = capacity

    # Getter
    @property
    def size(self):
        return self._size

    # Setter
    @size.setter
    def size(self, size):
        if not 0 <= size <= self.capacity:
            raise ValueError("Invalid number of cookies in the jar")
        self._size = size


def main():
    pass


if __name__ == "__main__":
    main()
