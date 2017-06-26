#!/usr/bin/python3
"""
Program that evaluates if a string of opening and closing braces are valid
Here are the examples from CodeWars:
validBraces( "(){}[]" ) => returns true
validBraces( "(}" ) => returns false
validBraces( "[(])" ) => returns false
validBraces( "([{}])" ) => returns true
"""
def checkGroups(char1, char2):
    parens = ["()", "[]", "{}"]
    for pair in parens:
        if char1 == pair[0] and char2 == pair[1]:
            return True
    return False

def validBraces(string):
    #we use a list as a stack because we're doing pretty simple stack operations
    stack = []
    openers = "{[("
    closers = "}])"
    for char in string:
        if char in openers:
            stack.append(char)
        else:
            if len(stack) < 1:
                return False
            else:
                openParen = stack.pop()
            if checkGroups(openParen, char) == False:
                return False
    if len(stack) > 0:
        return False
    return True

tests = ["[()]{}{[()()]()}", "[(])", "((()))", "([{}])", "[(])"]
for test in tests:
    print("testing: {}".format(test))
    print(validBraces(test))
