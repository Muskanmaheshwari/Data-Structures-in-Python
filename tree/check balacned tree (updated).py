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
def getHeigthAndcheckBalanced(root):
    if root==None:
        return 0, True
    lh,isleftBalanced = getHeigthAndcheckBalanced(root.left)
    rh,isrightBalanced = getHeigthAndcheckBalanced(root.right)
    h =1+max(lh,rh)
    if lh-rh>1or rh-lh>1:
        return h,False
    if isleftBalanced  and isrightBalanced:
        return h,True
    else:
        return h, False

root = inputTree()
printTree(root)
print(getHeigthAndcheckBalanced(root))
