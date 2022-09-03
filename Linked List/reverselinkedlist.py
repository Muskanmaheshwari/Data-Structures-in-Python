from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedListRec(head):
    # Your code goes here

    if head == -1 or head.next == -1:
        return head

    small_head = reverseLinkedListRec(head.next)

    temp = small_head
    while (temp.next is not None):
        temp = temp.next
    temp.next = head

    head.next = None

    return small_head

def reverse2approach(head):
    if head is None:
        return head,head
    if head.next is None:
        return head,head

    small_head, small_tail = reverse2approach(head.next)
    small_tail.next = head
    head.next = None
    return small_head,head

def reverse3approach(head):
    if head is None or head.next is None:
        return head
    small_head = reverse3approach(head.next)

    head.next.next = head
    head.next = None
    return small_head

def reverse(head):

    if head is None:
        return head
    # Write your code here
    prev = None
    pro = head
    temp = head
    while (temp is not None):
        pro = temp.next
        temp.next = prev
        prev = temp
        temp = pro
    head = prev
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
    #
    # newHead,tail = reverse2approach(head)
    # printLinkedList(newHead)
    nhead = reverse3approach(head)
    printLinkedList(nhead)

    t -= 1