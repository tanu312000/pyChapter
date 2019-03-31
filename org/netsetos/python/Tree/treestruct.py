class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def printPreorder(root):
    if(root != None):
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)


def printInorder(root):
    if(root!=None):
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)


def printPostorder(root):
    if (root != None):
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)



root = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)
nodeG = Node(7)



root.left=nodeB
root.right=nodeC
nodeB.left=nodeD
nodeB.right=nodeE
nodeC.left=nodeF
nodeC.right=nodeG


print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)



