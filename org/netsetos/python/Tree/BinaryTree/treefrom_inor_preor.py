class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def buildTree(in_arr,pre_arr,in_strt,in_end):
    preIndex=0
    print('in_strt',in_strt)
    print('in_end',in_end)
    if(in_strt>=in_end):
        return 0
    tNode=Node(pre_arr[preIndex])
    if(in_strt==in_end):
        return tNode
    inindex=search(in_arr,in_strt,in_end,tNode.data)
    tNode.left = buildTree(in_arr, pre_arr, in_strt, inindex-1)
    tNode.right = buildTree(in_arr, pre_arr, inindex+1, in_end)
    return tNode

def search(in_arr,instrt,inend,tNodedata):
    for i in range(instrt,inend):
        if(in_arr[i]==tNodedata):
            print('d--',in_arr[i])
            return i


inarr=[4 ,2 ,5 ,1 ,3]
prearr=[1 ,2 ,4 ,5 ,3]

buildTree(inarr,prearr,0,len(inarr)-1)





# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.right.left.right = Node(8)
# root.right.right.right = Node(9)
# print("Zigzag Order traversal of binary tree is",zigzagtraversal(root))