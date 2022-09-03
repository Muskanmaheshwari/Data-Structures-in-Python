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


def inputTree():
    rootdata = int(input("Enter your data: "))
    if rootdata==0:
        return

    root = tree(rootdata)
    leftree= inputTree()
    rightree = inputTree()
    root.left=leftree
    root.right=rightree
    return root

root = inputTree()
printTree(root)
