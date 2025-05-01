def factorial_loop(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(factorial_loop(5))  # Output: 120
print(factorial_loop(0))  # Output: 1