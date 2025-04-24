from math import *

def calculate(n):
    root = sqrt(n)
    print(f"the square root of {n} is: {root}")
    Logrithmic = log(n)
    print(f"the log of {n} is: {Logrithmic}")
    sine = sin(n)
    print(f"the sine of {n} is: {sine}")
    
n = int(input("Enter a number: "))
calculate(n)