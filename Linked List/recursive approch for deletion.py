from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNodeRec(head, pos):
    # Your code goes here
    if head is None:
        return head
    if pos == 0:
        temp = head.next
        head = None
        return temp
    if pos < 0:
        return head

    small_head = deleteNodeRec(head.next, pos - 1)
    head.next = small_head
    return head


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    pos = int(stdin.readline().rstrip())

    newHead = deleteNodeRec(head, pos)
    printLinkedList(newHead)

    t -= 1