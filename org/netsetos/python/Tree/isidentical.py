class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def isidentical(root1,root2):
    if(root1==None and root2==None):
        return True

    if(root1!=None and root2!=None and root1.data==root2.data):
        l=isidentical(root1.left,root2.left)
        r=isidentical(root1.right,root2.right)
        if(l and r):
            return True
    else:
        return False
    return False


root = Node("a")
nodeB = Node("b")
nodeC = Node("c")
nodeD = Node("d")
nodeE = Node("e")
nodeF = Node("f")
nodeG = Node("g")

root1 = Node("a")
nodeB1 = Node("b")
nodeC1 = Node("c")
nodeD1 = Node("d")
nodeE1 = Node("e")
nodeF1 = Node("f")
nodeG1 = Node("g")


root.left=nodeB
root.right=nodeC
nodeB.left=nodeD
nodeB.right=nodeE
nodeC.left=nodeF
nodeC.right=nodeG

root1.left=nodeB1
root1.right=nodeC1
nodeB1.left=nodeD1
nodeB1.right=nodeE1
nodeC1.left=nodeF1
nodeC1.right=nodeG1


print(isidentical(root1,root))