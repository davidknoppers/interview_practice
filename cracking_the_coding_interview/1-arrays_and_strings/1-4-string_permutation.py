#!/usr/bin/python3

"""
Program that checks if a string is a permutation of a palindrome
I.e. whether a string can be rearranged to form a palindrome
That's the case if an even-length string has all even character counts
E.g. 'aaddbbbb' -> 'adbbbbda'
Or an odd-length string has exactly one odd character counts
E.g. 'aadrr' -> 'radar'
"""

def check_string_permutation(string):
    if not string:
        return False
    if len(string) <= 1:
        return True
    #char_count tells us whether the string is even or odd length
    if len(string) % 2 == 0:
        char_count = "even"
    else:
        char_count = "odd"
    #we make a dict to track character counts; we use 0 to indicate an even
    #count for a char and 1 to indicate an odd count for a char
    count_dict = {}
    #this program is not case-sensitive; removing this line would make it so
    for char in string.lower():
        #1 means odd, 0 means even
        #the get method is the fastest add-or-update for a basic python dict
        count_dict[char] = count_dict.get(char, 0) + 1
        #if we just added 1 to 1, just set it to 0 to indicate the count is even
        if count_dict[char] > 1:
            count_dict[char] = 0
    #if it's an even-length string, all char counts must be even
    if char_count == "even":
        for val in count_dict.values():
            if val != 0:
                return False
        return True
    #if it's an odd-length string, we want exactly one odd char count
    odd_count_found = False
    for val in count_dict.values():
        if val != 0:
            if odd_count_found:
                return False
            else:
                odd_count_found = True
    if odd_count_found:
        return True
    return False
tests = ["radar", "abba", "AbAB", "rACEcaR", "", "a", "bb", "kay YAK",
         "akay YAK", "aaddrr", "aaddbbbb"]
for test in tests:
    print("{} -> {}".format(test, check_string_permutation(test)))
