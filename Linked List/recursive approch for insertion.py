class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def takeinput():
    temp,head = None, None
    inputList = [int(ele) for ele in input().split()]
    for currentNode in inputList:
        if currentNode == -1:
            break
        newnode = Node(currentNode)
        if head is None:
            head = newnode
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next  = newnode
    return head
def printLL(head):
    temp  = head

    while temp is not None:
        print(str(temp.data) + "->", end=' ')
        temp = temp.next
    print("None")

def insert_at_ith_pos(head, i,data):
    if i==0:
        newnode = Node(data)
        newnode.next = head
        return newnode
    if i<0:
        return head
    if head is None:
       return None

    small_head= insert_at_ith_pos(head.next, i-1, data)
    head.next = small_head
    return head

head = takeinput()
printLL(head)