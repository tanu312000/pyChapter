class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def H_T(self,root):

        if(root==None):
            return 0
        if(root.left==None and root.right==None):
            return 0
            l=H_T(root.left)
            r=H_T(root.right)
            if(l>r):
                return (1+l)
            return (1 + r)


    def H_T(self, root):

