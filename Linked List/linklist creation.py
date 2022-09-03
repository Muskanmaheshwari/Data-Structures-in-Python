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


head = takeinput()
printLL(head)