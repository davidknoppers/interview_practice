#!/usr/bin/python3

"""
Program that replaces spaces in a string with %20
You are given a string with some spaces and enough room at the end to fit
the extra characters you'll be including, e.g. 'amazon river  '
In real life I'd probably use string replace, but let's code it as CTCI intended!
We go backwards through the string (or char array, since we need to convert it to
manipulate it) and simply copies the string, except when our index i finds a space.
When it finds a space, it inserts '%20' instead
"""

def urlify(string):
    i = j = len(string) -1
    #strings are immutable so we need to convert our string into a char array
    string = list(string)
    #find the start of the string
    while string[i] == ' ' and i > 0:
    	  i -= 1
    #if the 'url' is just a bunch of whitespace, return None
    if i == 0:
        return None
    #i tracks the actual string, j tracks the spot where we push chars into our array
    while i > 0:
        if string[i] != ' ':
            swap_char = string[i]
            string[j] = swap_char
            i -= 1
            j -= 1
        else:
            string[j] = '0'
            string[j - 1] = '2'
            string[j - 2] = '%'
            j -= 3
            i -= 1
    #now that the array manipulations are done, we convert the char array back to str
    return ''.join(string)
tests = ["amazon river  ", "snoop doggy dogg    ", "camp lo thanksgiving sparkle      ", "         "]
for test in tests:
    print("{} -> {}".format(test, urlify(test)))
