#!/usr/bin/python3
"""
These are different iterations of the famous Largest Common Substring problem
"""
#just a terrible 2^n recursive solution
def lcs_bad(A, B, m, n):
    if m == 0 or n == 0:
        return 0
    elif A[m - 1] == B[n-1]:
        return 1 + lcs(A, B, m-1, n-1)
    else:
        return max(lcs(A, B, m, n - 1), lcs(A, B, m - 1, n))
#calculates the size of the largest common substring, but not the lcs itself
def lcs(A, B):
    m = len(A)
    n = len(B)
    arr = [[None]*(n+1) for i in range(m+1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif A[i-1] == B[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    for i in arr:
        print(i)
    return arr[m][n]
#modified version of the previous code that actually calculates the largest common substring
def lcs_str(A, B):
    m = len(A)
    n = len(B)
    arr = [[""]*(n+1) for i in range(m+1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                arr[i][j] = ""
            elif A[i-1] == B[j-1]:
                arr[i][j] = arr[i-1][j-1] + A[i-1]
            elif len(arr[i][j-1]) > len(arr[i-1][j]):
                arr[i][j] = arr[i][j-1]
            else:
                arr[i][j] = arr[i-1][j]
    return arr[m][n]

tests = [["abcdef", "abc"], ["132535365", "123456789"], ["a", "b"], ["", ""]]
for i in range(len(tests)):
    print(lcs_str(tests[i][0], tests[i][1]))
