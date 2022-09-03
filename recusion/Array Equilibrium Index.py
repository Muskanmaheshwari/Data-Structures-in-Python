from sys import stdin


def arrayEquilibriumIndex(arr, n):
    # Your code goes here
    if n == 0:
        return -1

    i = 0
    j = n - 1
    Sum = arr[i]
    rev = arr[j]
    # print(Sum, rev)
    while (i < j):

        if Sum < rev:
            i = i + 1
            Sum = Sum + arr[i]
            # print(Sum, rev)
        elif Sum > rev:
            j = j - 1
            rev = rev + arr[j]
            # print(Sum, rev)
        elif Sum == rev:
            i = i + 1
            j = j - 1
            Sum = Sum + arr[i]
            rev = rev + arr[j]
            # print(Sum, rev)


    if Sum == rev:
        return i
    else:
        return -1


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1