from sys import stdin


def rotate(arr, n, d):
    if len(arr)==0:
        print("0")
        return
    x= d%n-1
    i=x+1
    while(arr[x]!=arr[i%n]):
        print(arr[i%n], end=" ")
        i+=1
    print(arr[(i%n)+1])

# Your code goes here


# Taking Input Using Fats I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    # printList(arr, n)

    t -= 1