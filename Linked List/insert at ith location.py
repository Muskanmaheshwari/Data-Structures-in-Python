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
def insert_at_ith_node(head, i,data):
    if i < 0 or i>length(head):
        return head
    count=0
    temp = head
    prev = None
    while count<i:
        count+=1
        prev = temp
        temp = temp.next
    newnode = Node(data)
    if prev is not None:
        prev.next = newnode
    else:
        # newnode.next  = head
        head = newnode
    newnode.next = temp


    return head



    pass

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
        print(head.data,"->", end=" ")
        head = head.next

    print(None)


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    i = int(stdin.readline().rstrip())
    # printIthNode(head, i)
    head = insert_at_ith_node(head, i, 0)
    printLinkedList(head)
    t-=1