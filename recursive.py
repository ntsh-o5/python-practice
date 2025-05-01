def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

# Example usage
print(factorial_recursive(5))  # Output: 120
print(factorial_recursive(0))  # Output: 1