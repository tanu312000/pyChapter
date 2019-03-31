class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def getMirrorTree(root):
    if(root==None):
        return

    getMirrorTree(root.left)
    getMirrorTree(root.right)

    temp=root.left
    root.left=root.right
    root.right=temp

def printInorder(root):
    if(root!=None):
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)


root = Node("a")
nodeB = Node("b")
nodeC = Node("c")
nodeD = Node("d")
nodeE = Node("e")
nodeF = Node("f")
nodeG = Node("g")




root.left=nodeB
root.right=nodeC
nodeB.left=nodeD
nodeB.right=nodeE
nodeC.left=nodeF
nodeC.right=nodeG




data=getMirrorTree(root)
printInorder(data)
print(printInorder(root))