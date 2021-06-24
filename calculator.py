# Create a class called Calculator
class Calculator:

    # add
    def Add(self, num1, num2):
        return num1 + num2

    # subtract
    def Subtract(self, num1, num2):
        return num1 - num2

    # multiply
    def Multiply(self, num1, num2):
        return num1 * num2

    # divide
    def Divide(self, num1, num2):
        return num1 / num2


# Creating an object
calc = Calculator()
# Use object to call methods
print(calc.Add(2, 4))
print(calc.Subtract(2, 4))
print(calc.Multiply(2, 4))
print(calc.Divide(2, 4))

