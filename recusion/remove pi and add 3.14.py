def firstIndex(s):
    if len(s) == 0 or len(s) == 1:
        return s

    if (s[0]=="p" and s[1]=='i'):
        small = firstIndex(s[2:])
        return "3.14"+small
    else:
        small = firstIndex(s[1:])
        return s[0]+small

from sys import setrecursionlimit

setrecursionlimit(11000)
print(firstIndex('asdfghpisdppi'))
