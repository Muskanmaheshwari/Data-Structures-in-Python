def power(x, n):
    if n == 0 or x == 0:
        return 1
    if n % 2 == 0:
        s = power(x,n//2)
        return s*s
    else:
        s = power(x,n//2)
        return s*s*x

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
