class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def lowestcommonbt(self,root,p,q):

        if(root==None):
            return root
        if(root.data==p or root.data==q):
            return root

        left_lca=self.lowestcommonbt(root.left,p,q)
        right_lca=self.lowestcommonbt(root.right, p, q)

        if(left_lca != None and right_lca != None):
            return root

        if(left_lca != None):
            return left_lca
        else:
            return right_lca



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

    # for i in a:
    #     data = fp.insert(i)
    # print(data)

    data=fp.lowestcommonbt(root,4,5)
    print("Common lowest ancestor is",data.data)

