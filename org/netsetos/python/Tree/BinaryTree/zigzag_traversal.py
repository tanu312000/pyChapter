class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def zigzagtraversal(root):
    stack1=[]
    stack2=[]
    if (root==None):
        return False
    stack1.append(root)
    while(len(stack1)>0 or len(stack2)>0):
        while(len(stack1)>0):
            p=stack1.pop()
            print(p.data)
            if(p.left!=None):
                stack2.append(p.left)
            if(p.right!=None):
                stack2.append(p.right)
        while(len(stack2)>0):
            p=stack2.pop()
            print(p.data)
            if (p.right != None):
                stack1.append(p.right)
            if (p.left != None):
                stack1.append(p.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print("Zigzag Order traversal of binary tree is",zigzagtraversal(root))