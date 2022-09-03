from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    temp = head
    count = 0
    while (temp is not None):
        temp = temp.next
        count += 1
    return count


def swapNodes(head, i, j):
    # Your code goes here
    if (i == j):
        return head

    l = length(head)
    if (i > l or j > l or i < 0 or j < 0):
        return head
    p1 = None

    c = i

    while (c > 0):
        if (p1 is None):
            p1 = head
            c -= 1
        else:
            p1 = p1.next
            c -= 1
    if p1 is not None:
        c1 = p1.next
    else:
        c1 = head
    # print("c1",c1.data)
    p2 = None
    c = j
    while (c > 0):
        if (p2 is None):
            p2 = head
            c -= 1
        else:
            p2 = p2.next
            c -= 1
    if p2 is not None:
        c2 = p2.next
    else:
        c2 = head

    # print("c2",c2.data)
    if p1 != None:
        p2.next = c2
    else:
        head = c1
    if p2 != None:
        p2.next = c1
    else:
        head = c1
    if i == 0:
        temp = c2.next
        c2.next = c1.next
        p2.next = head
        head = c2
        c1.next = temp
    elif j == 0:
        temp = c2.next
        c2.next = c1.next
        c1.next = temp
        p2.next = c2
        head = c1

    if i - j == 1 or j - i == 1:
        temp = c2.next
        p1.next = c2
        c2.next = c1
        c1.next = temp

    else:
        temp = c1.next
        c1.next = c2.next
        c2.next = temp
        p1.next = c2
        p2.next = c1
    return head


# Taking Input Using Fast I/O
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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1