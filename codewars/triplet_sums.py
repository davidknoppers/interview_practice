#!/usr/bin/python3
#we import random to generate random arrays to test the algo
import random
"""
triplet_sums finds all groups in an array that add up to the target sum
The array and target are both supplied by the user
"""
def triplet_sums(arr, target):
    #sort the array to make subsequent subroutines much faster
    #we could also call set here if we don't want repeat terms in the array
    arr = sorted(arr)
    i = 0
    #result will hold our triplets
    result = []
    while i < len(arr) - 2:
        #one pointer starts at the beginning of the subarray, the other at the end
        start = i + 1
        end = len(arr) - 1
        #arr[i] is the starting point at each iteration in the loop. We sum arr[i]
        # with the elements at start and end and check what we get
        while start < end:
            _sum = arr[i] + arr[start] + arr[end]
            #if sum is too big, we decrement end
            if _sum > target:
                end -= 1
            #if sum is too small, we increment start
            elif _sum < target:
                start += 1
            #if the sum is a match, we try to put it in result(checking for dups first)
            #and then decrement end
            if _sum == target:
                if [arr[i], arr[start], arr[end]] not in result:
                    result.append([arr[i], arr[start], arr[end]])
                end -= 1
        i += 1
    return result
arr = []
for i in range(15):
    arr.append(random.randint(1, 15))
print("test array: {}".format(arr))
print("test array, sorted: {}".format(sorted(arr)))
print(triplet_sums(arr, 20))
