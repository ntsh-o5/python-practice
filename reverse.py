def reverse_string_recursive(s):
    if s == "":  # Base case: if the string is empty
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])  # Recursive case

print(reverse_string_recursive("hello")) 
 # Output: "olleh"
