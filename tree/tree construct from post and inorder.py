from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(postOrder, inOrder):
    if len(postOrder) == 0:
        return None
    rootdata = postOrder[len(postOrder) - 1]

    root = BinaryTreeNode(rootdata)
    rootIndexInOrder = -1
    for i in range(0, len(inOrder)):
        if inOrder[i] == rootdata:
            rootIndexInOrder = i
    if rootIndexInOrder == -1:
        return None

    leftInorder = inOrder[:rootIndexInOrder]
    rightInorder = inOrder[rootIndexInOrder + 1:]

    lengthlin = len(leftInorder)
    lengthrin = len(rightInorder)

    leftPostOrder = postOrder[0:lengthlin - 1]
    rightPostOrder = postOrder[lengthlin:lengthlin + lengthrin]

    leftchild = buildTree(leftPostOrder, leftInorder)
    rightchild = buildTree(rightPostOrder, rightInorder)
    root.left = leftchild
    root.right = rightchild
    return root


# Your code goes here


'''-------------------------- Utility Functions --------------------------'''


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder)
printLevelWise(root)
