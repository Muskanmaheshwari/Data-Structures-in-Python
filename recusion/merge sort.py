def mergecall(a, b, arr):
    i, j, k = 0, 0, 0
    while (len(a) > i and len(b) > j):
        if (a[i] > b[j]):
            arr[k] = b[j]
            j += 1
            k += 1
        elif a[i] < b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
    while (len(a) > i):
        arr[k] = a[i]
        i += 1
        k += 1
    while (len(b) > j):
        arr[k] = b[j]
        j += 1
        k += 1


def mergeSort(arr):
    # Please add your code here
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr) // 2
    a = arr[:mid]
    b = arr[mid:]
    mergeSort(a)
    mergeSort(b)
    mergecall(a, b, arr)


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
