#!/usr/bin/python3
"""
Python program that merges overlapping intervals
That means if you pass the program [[1, 3], [2, 4]] it will return [1, 4]
If that's hard to visualize, draw the intervals on a number line
This is a subproblem for many other problems, such as Calendar Conflicts
"""
def merge_intervals(arr):
    if not arr:
        return None
    if not isinstance(arr, list):
        return None
    if len(arr) < 1:
        return None
    result = []
    #sort the array by the first value in each subarray
    arr = sorted(arr)
    #loop through all subarrays
    for subarr in arr:
        #if our result is empty, just put the first subarray into the result
        if len(result) == 0:
            result.append(subarr)
        else:
            #we think of the most recently added subarray as on top of a "stack"
            #it'll stay there until it's merged with everything it can merge with
            subarr_on_stack = result[-1]
            #this is where we check if we can merge the subarrays
            #if the first number in this subarr is <= the second number in the stack,
            #then the intervals overlap and we should merge them
            if subarr[0] <= subarr_on_stack[1]:
                result[-1] = [subarr_on_stack[0], max(subarr_on_stack[1], subarr[1])]
            else:
                result.append(subarr)
    return result
testarr = [[1, 3], [2, 4]]
print("testarr: {}".format(testarr))
print(merge_intervals(testarr))
