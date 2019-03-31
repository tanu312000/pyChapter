class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def countRecur(root):
    if(root!=None):
        return(1+countRecur(root.left)+countRecur(root.right))
    else:
        return 0


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


print(countRecur(root))

