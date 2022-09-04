def partition(arr, start, end):
    count = 0
    pivot = arr[start]
    for i in range(start, end+ 1):
        if arr[i] < arr[start]:
            count += 1
    arr[count + start], arr[start] = arr[start], arr[count + start]
    st, en = start, end
    while st < en:
        if arr[st] < pivot:
            st += 1
        elif arr[en] >= pivot:
            en -= 1
        else:
            arr[st], arr[en] = arr[en], arr[st]
            st += 1
            en -= 1
    return start+count


def quickSort(arr, start, end):
    # Please add your code here
    if start >= end:
        return
    if start < end:
        i = partition(arr, start, end)
        quickSort(arr, start, i - 1)
        quickSort(arr, i + 1, end)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
# partition(arr, 0, len(arr) - 1)
quickSort(arr, 0, n-1)
print(*arr)
