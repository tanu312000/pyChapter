class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

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

    def lowest_common_ances_recu(self,root,p,q):
        if(root==0):
            return None
        if(root.data>p and root.data>q):
            return self.lowest_common_ances(root.left,p,q)
        if(root.data<p and root.data<q):
            return self.lowest_common_ances(root.right,p,q)

        return root

    def lowest_common_ances_iter(self,root,p,q):
        while(root!=0):
            if(root.data>p and root.data>q):
                root=root.left
            elif(root.data<p and root.data<q):
                root=root.right
            else:
                break
        return root

if __name__ == "__main__":
    fp = Tree()
    a = [8,3,1,6,4,7,10,14,13]
    for i in a:
        data = fp.insert(i)
    print(data)
    fp.inorder(fp.root)
    data=fp.lowest_common_ances_iter(fp.root,4,7)
    print("Common lowest ancestor is",data.data)
