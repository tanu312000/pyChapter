class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def printNodes(self, root,k,dist):
        if(root != None):
            if(k==dist):
                print(root.data)
                return
            self.printNodes(root.left, k, dist+1)
            self.printNodes(root.right, k, dist + 1)

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')
root.left.left.left = Node('h')
root.left.left.right = Node('i')
root.left.right.left = Node('j')
root.left.right.right = Node('k')
root.right.left.left = Node('l')
root.right.left.right = Node('m')
root.right.right.left = Node('n')
root.right.right.right = Node('o')

if __name__ == "__main__":
    fp = Tree()
    data=fp.printNodes(root,3,0)
    print(data)