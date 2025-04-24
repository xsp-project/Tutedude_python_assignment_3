def factorial(n):
    
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter a number: "))
result = (f"factorial of {n} is {factorial(n)}")
print(result)