class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

def printTree(root):
    if root == None:
        return
    print("root data",root.data,":",end="")
    if root.left != None:
        print("L",root.left.data,end=",")
    if root.right != None:
        print("R",root.right.data)
    else:
        print()
    printTree(root.left)
    printTree(root.right)

btn1 = tree(1)
btn2 = tree(2)
btn3 = tree(3)
btn1.left = btn2
btn1.right = btn3

printTree(btn1)


