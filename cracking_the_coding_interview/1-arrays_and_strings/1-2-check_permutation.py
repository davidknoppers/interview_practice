#!/usr/bin/python3

"""
Check if two strings are permutations of one another
As addressed in the book, this is very easy and readable to
do with sorting; just return sorted(s1) == sorted(s2)
That's O(n*log(n)) time and O(1) auxiliary space
But let us labor through the O(n) space, O(n) time solution
"""

def check_string_perm(s1, s2):
    #s1 is string 1, s2 is string 2
    #they won't be permutations of each other if they're not the same length
    if len(s1) != len(s2):
        return False
    #make a dict of character counts of s1
    count_dict = {}
    for char in s1:
        count_dict[char] = count_dict.get(char, 0) + 1
    #loop through the second string; if the character is in the dict, subtract 1
    #else, set the value to -1
    for char in s2:
        count_dict[char] = count_dict.get(char, 0) - 1
        #if the value for any char is -1, either there are too many of a char in s2
        #or there's a char in s2 that wasn't in s1
        if count_dict[char] < 0:
            return False
    #if we made it through s2 without returning False, we must have permutations
    return True


tests = [["abbcccddddeeeee", "eeeeeddddcccbba"], ["", ""], ["abbcccddddeeeee", "eeeeeddddcbba"], ["abba", "ABBA"], ["radar", "rraad"]]
for test in tests:
    print("s1: {}\ns2: {}\nresult: {}".format(
        test[0], test[1], check_string_perm(test[0], test[1])))
