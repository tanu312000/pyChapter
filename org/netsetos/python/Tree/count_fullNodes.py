class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def count_fullNodes(root):
    if(root==None):
        return 0
    if(root.left==None and root.right==None):
        return 0
    if(root.left!=None and root.right!=None):
        return (1+count_fullNodes(root.left)+count_fullNodes(root.right))
    else:
        return count_fullNodes(root.left)+count_fullNodes(root.right)


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


print(count_fullNodes(root))
