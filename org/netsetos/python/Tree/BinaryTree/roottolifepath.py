class Node:

    def __init__(temp, data):
        temp.left = None
        temp.right = None
        temp.data = data


class Tree:

    def inorder(self,root,arr):
        if(root!=None):
            arr.append(root.data)
            self.inorder(root.left,arr)
            if(root.left==None and root.right==None):
                print(arr)
            self.inorder(root.right,arr)
            arr.pop()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    fp = Tree()

    arr=[]
    data=fp.inorder(root,arr)
    print(data)

