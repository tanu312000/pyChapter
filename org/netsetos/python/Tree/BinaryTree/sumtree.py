class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

class sumTree:
    def SumTree(self,p):
        if(p==None):
            return -1
        if(p.left==None and p.right==None):
            return p.data

        leftSum=self.SumTree(p.left)
        rightSum=self.SumTree(p.right)

        if(leftSum == -1 or rightSum == -1):
            return -1
        if(p.data == leftSum + rightSum):
            return 2*p.data
        return -1


root = Node(50)
root.left = Node(15)
root.right = Node(11)
root.left.left = Node(10)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(3)

if __name__ == "__main__":
    fp = sumTree()
    data=fp.SumTree(root)
    print(data)

