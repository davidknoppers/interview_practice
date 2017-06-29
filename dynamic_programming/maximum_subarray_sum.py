#!/usr/bin/python3

"""
Standard implementation of Kadane's Algorithm
"""

def maxSequence(arr):
    #basic cases - if there's no array, if the array is empty, and if the array is all < 0
    if not arr:
        return 0
    if len(arr) < 1:
        return 0
    #flag to check if we've found a nonzero positive number
    positive_found = None
    for num in arr:
        if num > 0:
            positive_found = 1
            break
    #if no nonzero positive number is found, the best we can do is 0
    if not positive_found:
        return 0
    #initialize a var to track current sum and best sum seen
    current_sum = 0
    max_so_far = 0
    for num in arr:
        #if the current sum is 0 or more, it *might* be good for us to hold on
        #to the current values, so we hold them until the sum goes below 0
        if current_sum + num >= 0:
            current_sum += num
        else:
            current_sum = 0
        if current_sum > max_so_far:
            max_so_far = current_sum
    return max_so_far
#some basic test cases
test_arrs = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [-2, -3, 4, -1, -2, 1, 5, -3], [], None]
for arr in test_arrs:
    print("Max sum of {}\nIs: {}".format(arr, maxSequence(arr)))
