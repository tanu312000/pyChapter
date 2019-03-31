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

def isubtree(t1,t2):
    if(t1==None):
        return True
    if (t2==None):
        return False
    if(isidentical(t1,t2)):
        return True
    m=isubtree(t1.left,t2)
    n=isubtree(t1.right,t2)
    return  m or n

root1 = Node('a')
root1.left = Node('b')
root1.right = Node('c')
root1.left.left = Node('d')
root1.left.right = Node('e')
root1.right.left = Node('f')
root1.right.right = Node('g')

root2 = Node('a')
root2.left = Node('b')
root2.left.left = Node('d')
root2.left.right = Node('e')






print(isubtree(root1,root2))