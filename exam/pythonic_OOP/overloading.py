class Calculator:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

calc = Calculator()
print(calc.add(1, 2))  # prints 3
print(calc.add(1, 2, 3))  # prints 6
