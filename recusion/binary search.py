from sys import setrecursionlimit
def binarysearch(a,x,si,ei):
    if si>ei:
        return -1
    mid = (ei + si)//2
    if a[mid] == x:
        return mid
    elif x>a[mid]:
        si = mid+1
        return binarysearch(a,x,si,ei)
    elif x<a[mid]:
        ei = mid-1
        return binarysearch(a,x,si,ei)
setrecursionlimit(11000)
a = [1,3,5,7,9,11,13,15,16,17]
print(binarysearch(a,9,0,len(a)))