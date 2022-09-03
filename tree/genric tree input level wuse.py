import queue
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def takeinputlevelwise():
    q = queue.Queue()
    print("Enter root data")
    rootdata = int(input())
    if rootdata == -1 :
        return None
    root = treeNode(rootdata)
    q.put(root)
    while(not (q.empty())):
        cu = q.get()
        print("Enter number of children of", cu.data,"have.")
        num = int(input())
        for i in range(num):
            print("Enter child of",cu.data,":")
            childdata = int(input())
            child = treeNode(childdata)
            cu.children.append(child)
            q.put(child)
    return root
    pass

x=takeinputlevelwise()
