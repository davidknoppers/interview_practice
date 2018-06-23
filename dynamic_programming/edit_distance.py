#!/usr/bin/python3
"""
Classic dynamic programming algorithm
This is the vanilla algo, i.e. all string operations are considered 1 step
Fastest solution is O(m*n) in time and auxilary space, where n and m
are the lengths of each of the two strings
"""
def edit_distance(str1, str2):
    """
    Initialize a 2D array that will hold the number of edits required to go from
    one string to the other
    """
    m = len(str1)
    n = len(str2)
    if m == 0:
        return n
    if n == 0:
        return m
    edit_array = [[0 for i in range(n)] for j in range(m)]
    #loop through every element in the 2D array
    #this will have the effect of comparing one char at a time
    for i in range(m):
        for j in range(n):
            #if one string is empty, the edit distance is the length of the other string
            if i == 0:
                edit_array[i][j] = j
            #just like the i == 0 case above this, but for  j == 0
            elif j == 0:
                edit_array[i][j] = i
            #if the characters at this point in both strings are equal, the edit distance shouldn't increase
            #so we just take minimum edit distance possible at that point
            elif str1[i] == str2[j]:
                edit_array[i][j] = min(edit_array[i-1][j], edit_array[i][j-1], edit_array[i - 1][j - 1])
            #if the characters are different, we need to add 1 to the edit distance
            else:
                edit_array[i][j] = min(edit_array[i-1][j], edit_array[i][j-1], edit_array[i - 1][j - 1]) + 1
    for row in edit_array:
        print((row))
    return edit_array[m - 1][n - 1]
tests = [["goal", "gold"], ["east", ""], ["daft punk", "of montreal"], ["hollow", "hallow"]]
for test in tests:
    print("{} and {} returns edit distance of {}".format(test[0], test[1], edit_distance(test[0], test[1])))
