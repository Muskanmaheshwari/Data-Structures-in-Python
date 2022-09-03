# Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array. Return -1 if it is not present in the array.
# First index means, the index of first occurrence of x in the input array.
# Do this recursively. Indexing in the array starts from 0.

def firstIndex(arr, x, n, si):
    # Please add your code here
    # print(si)
    if si == n:
        return -1
    elif arr[si] == x:
        return si
    else:
        return firstIndex(arr, x, n, si + 1)


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
si = 0
print(firstIndex(arr, x, n, si))
