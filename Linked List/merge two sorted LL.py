from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None





def Merge(head1, head2):
    # Write your code here
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    ft, fh = None, None
    if head1.data >= head2.data:
        ft, fh = head2, head2
        head2 = head2.next
    else:
        ft, fh = head1, head1
        head1 = head1.next
    while (head1 is not None and head2 is not None):
        if (head1.data < head2.data):
            ft.next = head1
            head1 = head1.next
            ft = ft.next
        elif (head1.data >= head2.data):
            ft.next = head2
            head2 = head2.next
            ft = ft.next
    if head1 is not None:
        ft.next = head1
        head1 = head1.next
        ft = ft.next
    elif head2 is not None:
        ft.next = head2
        head2 = head2.next
        ft = ft.next
    return fh
def middle(head):
    if head is None:
        return None
    slow = head
    fast = head
    while (fast.next is not None and fast.next.next is not None):
        # print(slow.data)
        slow = slow.next
        fast = fast.next.next
    # print(slow.data)
    return slow

def mergeSort(head):
    # Your code goes here
    if head is None or head.next is None:
        return head
    # print("Iam going to get the mid")
    mid = middle(head)
    # print(mid.data)
    head2 = mid.next
    mid.next = None

    nh1=mergeSort(head)
    nh2=mergeSort(head2)
    return Merge(nh1, nh2)



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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1