class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def is_Complete_Binary(root):
    if(root==None):
        return True
    if(root.left==None and root.right==None):
        return True
    if(root.left!=None and root.right!=None):
        l=is_Complete_Binary(root.left)
        r=is_Complete_Binary(root.right)
        return (l and r)
    else:
        return False


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


nodescount=print(is_Complete_Binary(root))
print(nodescount)
