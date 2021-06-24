# Functional Calculator

## Summary

Lets make a functional calculator.

## Tasks

* Complete the core tasks

```python
# Create a class called Calculator
# functions
# practice using, defining and calling functions

# Build a basic functional
# Core 1: build function containing
    # add,
    # subtract,
    # multiply,
    # divide.

# Create a file for child class called Functional_calculator
# import calculator class and inherit all the functionality 
# Core 2: Build more functions for
    # area of a circle
    # area of a square
    # area of a triangle (just find the easiest way)
```

```python
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
```
Will return:
```python
6
-2
8
0.5
```