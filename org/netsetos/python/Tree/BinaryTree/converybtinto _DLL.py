class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

class BinaryToDoubleLinkedList:
    def BinaryToDLL(self,root):
       if (root.left != None):
           ltree=self.BinaryToDLL(root.left)
           while(ltree.right!=None):
               ltree=ltree.right
           ltree.right=root
           root.left=ltree

       if(root.right!=None):
           rtree = self.BinaryToDLL(root.right)
           while (rtree.left != None):
               rtree=rtree.left
           rtree.left=root
           root.right=rtree
       return root

    def go_left(self, root):
        temp=root
        while(temp.left!=None):
            temp=temp.left
        return temp

    def traverse(self,head):
        temp=head
        while(temp.right!=None):
            print("Data is",temp.data)
            temp=temp.right
        return head         



root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')

if __name__ == "__main__":
    fp = BinaryToDoubleLinkedList()
    data=fp.BinaryToDLL(root)
    changrot=fp.go_left(data)
    fp.traverse(changrot)