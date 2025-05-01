Code

def sum_of_digits_loop(n):
    n = abs(n)  # Handle negative numbers
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit to the total
        n //= 10  # Remove the last digit
    return total

# Example usage
print(sum_of_digits_loop(1234))  # Output: 10
print(sum_of_digits_loop(-567))   # Output: 18