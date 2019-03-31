class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def remove_Nodes(self,root,k):
        if(root==None):
            return 0
        if(k==0):
            return root
        root.left=self.remove_Nodes(root.left,k-1)
        root.right = self.remove_Nodes(root.right, k - 1)
        if(root.left==None and root.right==None):
            return None
        return None
    def printPreorder(self):



root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')

if __name__ == "__main__":
    fp = Tree()
    data=fp.remove_Nodes(0,'a')
    print(data)