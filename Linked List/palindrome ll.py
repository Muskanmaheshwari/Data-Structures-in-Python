from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isPalindrome(head):
    # Your code goes here
    if head is None:
        return True
    if head.next is None:
        return True
    count = 1
    slow, fast = head, head
    while (fast.next is not None and fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next
        count += 1
    head2 = slow.next
    slow.next = None
    prev = None
    pro = head2
    temp = head2
    while (temp is not None):
        pro = temp.next
        temp.next = prev
        prev = temp
        temp = pro
    head2 = prev



    while (head2 is not None):
        # print(head.data,head2.data)
        if (head.data == head2.data):

            head=head.next
            head2=head2.next
        else:
            return False

    return True


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


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1