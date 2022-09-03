from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head) :
    #Your code goes here
    # temp = None
    count=0
    temp = head
    while temp is not None:
        count+=1
        temp = temp.next
    return count



def printIthNode(head, i):
    # Your code goes here
    temp = head
    max_count = length(head)

    count = 0
    if head is None:
        return
    elif ((i > max_count) or (i <0)):
        return
    else:
        while (count < i):
            temp = temp.next
            count += 1
    print(temp.data)


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
    i = int(stdin.readline().rstrip())
    printIthNode(head, i)

    t -= 1