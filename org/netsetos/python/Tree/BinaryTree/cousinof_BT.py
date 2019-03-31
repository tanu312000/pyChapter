class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def isSibling(self,root, a, b):
        if root is None:
            return False

        x=False
        y=False
        z=False
        if(root.left!=None and root.right!=None):
            if((root.left.data == a and root.right.data == b)or(root.left.data == b and root.right.data == a)):
                x=True
        if (root.left != None):
            y=self.isSibling(root.left,a,b)
        if(root.right != None):
            z=self.isSibling(root.right,a,b)
        return x or y or z


            # def Sibling(self,root,a,b):
    #     if(root==None):
    #         return 0
    #     return((root.left==a and root.right==b)or(root.left==b and root.right==a)or
               #self.Sibling(root.left, a, b) or self.Sibling(root.right, a, b))

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


    def Cousin(self,root,a,b):
        levelFirstElement=self.getLevel(root,1,a)
        levelSecondElement=self.getLevel(root,1,b)
        if(levelFirstElement and levelSecondElement):
            if(self.isSibling(root,a,b)):
                return False
            else:
                return True


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

if __name__ == "__main__":
    fp = Tree()
    data=fp.Cousin(root,4,5)
    # level=fp.getLevel(root,1,'g')
    print(data)