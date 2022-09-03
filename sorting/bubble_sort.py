def bubble(b,a):
    for i in range(a,0,-1):
        for j in range(0,i-1):
            if (b[j]>b[j+1]):
                b[j],b[j+1]=b[j+1],b[j]


    return b
    pass
a = int(input())
b=list(map(int, input().split(" ")))
x=bubble(b,a)
print(x)
