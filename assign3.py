from math import *
num = float(input("Enter a number: "))
if num < 0:
    raise ValueError("Cannot compute square root of negative number")
else:
    print(f"The square root of {num} is {sqrt(num)}")
    print(f"The Natural Logarithm of {num} is {log(num)}")
    print(f"The Sine of {num} is {sin(num)}")
