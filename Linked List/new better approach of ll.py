class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def take_input():
    head, temp = None, Node
    inputList = [ int(ele) for ele in input().split()]
    for current_node in inputList:
        if current_node == -1:
            break
        newnode = Node(current_node)
        if head is None:
            head = newnode
            temp = newnode
        else:
            temp.next  = newnode
            temp = newnode
    return head
def printLL(head):
    temp  = head

    while temp is not None:
        print(str(temp.data) + "->", end=' ')
        temp = temp.next
    print("None")
head  = take_input()
printLL(head)
