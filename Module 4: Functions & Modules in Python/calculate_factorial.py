# Task 1: Calculate Factorial Using a Function
n = int(input("Enter a number:"))

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        print(1)  # Base case: factorial of 0 or 1 is 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
            print(f"Factorial of {n}: {result}")


factorial(n)  # Example usage, should return 120
