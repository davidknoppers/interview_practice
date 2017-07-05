#!/usr/bin/python3

"""
Implement a function to determine if a string is unique
A string is unique if it has no repeating characters
"""
def is_unique(string):
    #make a set to store seen characters
    #set will use O(n) space, where n is the number of unique characters in the string
    #this algo assumes lowercase != uppercase; that's easy to change if need be
    seen_set = set()
    for char in string:
        #set lookup is constant, so this algo's runtime is linear to the length of string
        if char in seen_set:
            return False
        else:
            seen_set.add(char)
    return True
tests = ["abcdefghjikl123456789", "", "1234567654", "abccdefghijklmnop", "aAbBcC"]
for test in tests:
    print("test: {}\nresult:{}".format(test, is_unique(test)))
