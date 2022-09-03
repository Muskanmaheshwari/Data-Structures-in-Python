def insertion_sort(b,a):
    for i in range(1,a):
        key=b[i]
        j=i-1
        while(b[j]>key and j>=0):
            b[j+1]=b[j]
            j-=1
        b[j+1]=key
    return b
    pass
a = int(input())
b=list(map(int, input().split(" ")))
x= insertion_sort(b,a)
print(x)