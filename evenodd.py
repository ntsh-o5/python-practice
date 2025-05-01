
Code

def is_even_or_odd_recursive(num):
    if num < 0:
        num = -num  # Handle negative numbers
    if num == 0:
        return "Even"
    elif num == 1:
        return "Odd"
    else:
        return is_even_or_odd_recursive(num - 2)

# Example usage
print(is_even_or_odd_recursive(4))  # Output: Even
print(is_even_or_odd_recursive(7))  # Output: Odd