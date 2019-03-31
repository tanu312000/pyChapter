class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Binary_Tree:
    def minDepth(self, root):

        if (root == None):
            return 0
        elif(root.left==None and root.right==None):
            return 1
        elif (root.left != None and root.right == None):
            l =1+self.minDepth(root.left)

            return l
        elif (root.left == None and root.right != None):
            r = 1 + self.minDepth(root.right)
            return r
        return min(1 + self.minDepth(root.right),1 + self.minDepth(root.left))

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
    fp = Binary_Tree()

    # for i in a:
    #     data = fp.insert(i)
    # print(data)
    #fp.inorder(fp.root)
    data = fp.minDepth(root)
    print("Minimum Depth of Tree is", data)


