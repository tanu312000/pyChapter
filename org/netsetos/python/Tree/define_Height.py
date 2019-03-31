class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def Height_tree(root):
    if(root==None):
        return 0
    if (root.left == None and root.right==None):
        return 0
    l=Height_tree(root.left)
    r= Height_tree(root.right)



    if (l>r):
        n = l
    else:
        n = r
    return(1+n)

    def maxDepth(self, A):
        if (A == None):
            return 0
        if (A.left == None and A.right == None):
            return 0
        else:
            if (maxDepth(A.left) > maxDepth(A.right)):
                return (1 + maxDepth(A.left))
            else:
                return (1 + maxDepth(A.right))





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
nodeD.left = nodeF
#nodeC.right = nodeG

print(Height_tree(root))