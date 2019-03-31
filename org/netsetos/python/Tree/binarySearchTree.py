class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def search(self,root,elementSearch):

        if(root==None):
            return root
        if(elementSearch<root.data):
            return self.search(root.left,elementSearch)
        else:
            return self.search(root.right, elementSearch)
        return root

    def insert(self, data):
        if(self.root == None):
            self.root=Node(data)

        else:
            p = self.root
            q = data
            while (1):
                if (q < p.data):
                    if (p.left == None):
                        p.left = Node(q)
                        break
                    else:
                        p = p.left
                elif(q > p.data):
                    if (p.right == None):
                        p.right = Node(q)
                        break
                    else:
                        p = p.right


                else:
                    break



    def inorder(self,root):
        if (root!=None):
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

if __name__ == "__main__":
    fp = Tree()
    a = [12, 18, 11, 1, 3, 20, 17, 19]
    # for i in a:
    #     data = fp.insert(i)
    # print(data)
    #fp.inorder(fp.root)
    data=fp.search(fp.root,7)
    print("Searched Element",data.data)
