#!/usr/bin/python3
"""
This code calculates a fibonacci number with a slightly different algo
Instead of summing the two previous terms, we sum term n-2 with term n-1... squared

"""
def fib_modified(first, second, num_terms):
    """
    first is the first term in the sequence
    second is the second term in the sequence
    Both first and second will be passed by user
    num_terms is the number of terms you want the function to calculate
    fib_mod, below, is the "modified" line for the fibonacci calculation
    """
    fib_mod = lambda x, y: x + y**2

    for i in range(num_terms - 2):
        next_term = fib_mod(first, second)
        first = second
        second = next_term
        #print(next_term)
    return next_term
print(fib_modified(0, 1, 5))
