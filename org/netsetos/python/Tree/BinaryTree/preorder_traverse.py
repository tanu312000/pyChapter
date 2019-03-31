class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class Tree:
    def __init__(self):  # constr
        self.root = None

    def preorderTraversal(self, root):
        output=[]
        if(root==None):
            return root
        nodestack=[]
        nodestack.append(root)
        while(len(nodestack)>0):
            node=nodestack.pop()
            print(node.data)
            if(node.right!=None):
                nodestack.append(node.right)
            if(node.left!=None):
                nodestack.append(node.left)
        print(output)

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

    # for i in a:
    #     data = fp.insert(i)
    # print(data)
    #fp.inorder(fp.root)
    data = fp.preorderTraversal(root)
    print("Preorder Traverse is", data)

