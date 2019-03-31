from collections import OrderedDict


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def left_view(self, root, level,maxlevel):

        if (root != None):
            if (maxlevel[0] < level):
                print(root.data)
                maxlevel[0]=level

            self.left_view(root.left, level + 1, maxlevel)
            self.left_view(root.right, level + 1,maxlevel)


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')

if __name__ == "__main__":

    maxlevel = [0]


    fp = Tree()

    data = fp.left_view(root,1, maxlevel)
    print(data)
