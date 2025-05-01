def sum_of_elements_loop(lst):
    #the 'def' defines the 'sum_of_elements_loop' function, which is calculating the sum of all elements in a list using simple loop.
    total = 0
    for element in lst:
    #'1st' is the parameter of the function.
        total += element
    return total

numbers = [1, 2, 3, 4, 5]
print(sum_of_elements_loop(numbers)) 
     # Output being 15 = 1+2+3+4+5
