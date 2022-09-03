import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(lst):
    if len(lst) == 0:
        return None
    mid = (len(lst) - 1) // 2
    x = BinaryTreeNode(lst[mid])
    root = x
    leftroot = constructBST(lst[:mid])
    rightroot = constructBST(lst[mid + 1:])
    root.left = leftroot
    root.right = rightroot
    return root
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
if (n > 0):
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst)
preOrder(root)