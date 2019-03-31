class Node:

    def __init__(temp, data):
        temp.left = None
        temp.right = None
        temp.data = data


class Tree:

    def converttree(self,root):
        if(root ==None or root.right ==None or root.left ==None):
            return None
        else:
            self.converttree(root.left)
            self.converttree(root.right)

            if(root.left !=None):
                leftdata=root.left.data
            if(root.right != None):
                rightdata=root.right.data

            diff=rightdata+leftdata-root.data

            if(diff>0):
                root.data=root.data+diff
            if(diff<0):
                self.increment(root, -diff)
        return root

    def increment(self,root,diff):
        if(root!=None):
            if (root.left != None):
                root.left.data = root.left.data + diff
                self.increment(root.left, diff)
            elif(root.right!=None):
                root.right.data = root.right.data + diff
                self.increment(root.right, diff)
            return root

    def preorder(self,root):
        if(root!=None):
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)









root = Node(55)
root.left = Node(10)
root.right = Node(25)
root.left.left = Node(9)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(11)
root.right.left.right = Node(14)

if __name__ == "__main__":
    fp = Tree()

    # for i in a:
    #     data = fp.insert(i)
    # print(data)

    data=fp.converttree(root)
    data1=fp.preorder(data)
    print(data1)


