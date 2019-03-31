class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def evaluationtree(root):
    if (root != None):
        if(root.left==None and root.right==None):
            return root.data

        leftsum=evaluationtree(root.left)
        rightsum =evaluationtree(root.right)

        if(root.data=='+'):
            return leftsum+rightsum
        if (root.data == '-'):
            return leftsum - rightsum
        if (root.data == '*'):
            return leftsum * rightsum
        if (root.data == '/'):
            return leftsum / rightsum






if __name__ == "__main__":
    root = Node('+')
    root.left = Node('/')
    root.left.left = Node('*')
    root.left.left.left = Node(10)
    root.left.left.right = Node(2)
    root.left.right = Node(5)
    root.right = Node('-')
    root.right.left = Node(100)
    root.right.right = Node('*')
    root.right.right.left = Node(3)
    root.right.right.right = Node(30)


    data=evaluationtree(root)
    print(data)












