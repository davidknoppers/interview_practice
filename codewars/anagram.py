#!/usr/bin/python3
"""
This function returns True if two strings are anagrams of each other, False otherwise
It does this by building dictionaries for each word, containing counts of each character
"""
def anagram_check(s1, s2):
    #for this challenge I was instructed to make False the default return value
    #if the input was invalid
    if not s1 or not s1:
        return False
    if not isinstance(s1, str) or not isinstance(s2, str):
        return False
    #initialize dictionaries for strings 1 and 2
    s1_dict = {}
    s2_dict = {}
    #loop through each string and add or update values
    #the dictionary get method is known to be a fast way to check for existence,
    #then update the value
    for char in s1:
        s1_dict[char] = s1_dict.get(char, 0) + 1
    for char in s2:
        s2_dict[char] = s2_dict.get(char, 0) + 1
    #python makes it extremely easy to see if our dictionaries contain the same
    #values after we've built them
    return s1_dict == s2_dict


#some basic tests
tests = [["abba", "baba"], ["jones", ""], ["racecar", "car race"],
         ["bade beads", "abed bade"], ["calipers", "replicas"],
         ["rasp rashes rattles", "raps shares startle"], [5, 4]]
for test in tests:
    print("String 1: {}\nString 2: {}".format(
        test[0], test[1]))
    print("Result: {}".format(anagram_check(test[0], test[1])))
