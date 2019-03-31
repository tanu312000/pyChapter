class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diagonal_traversal(root,diag,dict):

    if (root != None):
        diagonal_traversal(root.left,diag+1,dict)
        diagonal_traversal(root.right,diag,dict)

        if(dict.get(diag)!=None):
            dict[diag].append(root.data)
        else:
            dict[diag]=[root.data]

    return dict





if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(8)
    root.right.right.left = Node(9)
    root.left.right = Node(5)
    root.left.right.right = Node(7)
    root.left.right.left = Node(6)

    dict={}
    dict=diagonal_traversal(root,0,dict)
    print(dict)












