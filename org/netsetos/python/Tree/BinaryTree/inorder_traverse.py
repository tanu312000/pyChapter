class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class Tree:
    def __init__(self):  # constr
        self.root = None

    def inorderTraversal(self, root):
        if(root == None):
            return root
        traverse_list=[]
        stack=[]
        current=root
        while(current!=None or len(stack)>0):
            while(current!=None):
                stack.append(current)
                current=current.left
            if(len(stack)>0):
                node=stack.pop()
                traverse_list.append(node.data)
                current=node.right
        return traverse_list

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
    data = fp.inorderTraversal(root)
    print("Inorder Traverse is", data)
