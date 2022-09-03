def selection_sort(b,a):
    for i in range(0,a):
        min=i
        for j in range(i+1,a):
            if b[min]>b[j]:
                min=j
        if min!=i:
            b[min],b[i]=b[i],b[min]
    return b

    pass
a = int(input())
b=list(map(int, input().split(" ")))
x= selection_sort(b,a)
print(x)