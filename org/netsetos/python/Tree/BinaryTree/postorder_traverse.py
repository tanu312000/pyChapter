class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class Tree:
    def __init__(self):  # constr
        self.root = None

    def postorderTraversal(self, root):
        if(root == None):
            return root
        stack=[]
        while(True):
            while(root!=None):
                if(root.right!=None):
                    stack.append(root.right)
                stack.append(root)

                root=root.left

            root=stack.pop()

            if(root.right != None and len(stack)>0 and stack[-1] == root.right):
                stack.pop()
                stack.append(root)
                root=root.right
            else:
                print(root.data)
                root=None

            if(len(stack) <=0):
                break

root = Node("a")
nodeB = Node("b")
nodeC = Node("c")   
nodeD = Node("d")
nodeE = Node("e")
nodeF = Node("f")
nodeG = Node("g")



root.left=nodeB
root.right=nodeC
nodeB.left=nodeD
nodeB.right=nodeE
nodeC.left=nodeF
nodeC.right=nodeG

if __name__ == "__main__":
    fp = Tree()
    data = fp.postorderTraversal(root)
    print("Postorder Traverse is", data)


