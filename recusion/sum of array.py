def sumArray(arr,n):
    # Please add your code here
    if n<=0:
        return 0
    s = sumArray(arr, n-1)+ arr[n-1]
    return s

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr,n))