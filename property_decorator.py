class MyClass:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        """Getter for value."""
        return self.__value

    @value.setter
    def value(self, new_value):
        """Setter for value."""
        if new_value < 0:
            raise ValueError("Value must be non-negative!")
        self.__value = new_value

    @value.deleter
    def value(self):
        """Deleter for value."""
        del self.__value


# Usage
obj = MyClass(10)
print(obj.value)  # Calls the getter
obj.value = 20    # Calls the setter
print(obj.value)
# del obj.value     # Calls the deleter
