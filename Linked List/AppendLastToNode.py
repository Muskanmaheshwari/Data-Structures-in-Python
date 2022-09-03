
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def length(head):
    # Your code goes here
    temp = None
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count


def appendLastNToFirst(head,tail, n) :
    #Your code goes here
    if head is None or head.next is None:
        return head
    x=length(head)-n
    while(x>0):
        tail.next=head
        head=head.next
        tail=tail.next
        tail.next=None
        x=x-1
    return head






#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head, tail


#to print the linked list
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head,tail = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head,tail,n)
    printLinkedList(head)

    t -= 1