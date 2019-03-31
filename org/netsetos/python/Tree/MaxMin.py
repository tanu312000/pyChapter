class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def FindMin(root):
    if(root==None):
        return 0
    temp=root
    while(temp.left!=None):
        temp=temp.left
    return temp.data

root = Node("a")
nodeB = Node("b")
nodeC = Node("c")
nodeD = Node("d")
nodeE = Node("e")
nodeF = Node("f")
nodeG = Node("g")

root.left = nodeB
root.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.left = nodeF
nodeC.right = nodeG

print(FindMax(root))

