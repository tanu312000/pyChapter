class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def getLevel(self,root,level,key):
        self.root=root
        if(root==None):
            return 0
        if(root.data==key):
            return level
        dwnlevel=self.getLevel(root.left,level+1,key)
        if(dwnlevel!=0):
            return dwnlevel
        return self.getLevel(root.right,level+1,key)

    def  getLevl(self,root,key):
        return self.getLevl(root,1,key)

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')

if __name__ == "__main__":
    fp = Tree()
    data=fp.getLevel(root,0,'f')
    print(data)