class Node:

    def __init__(temp, data):
        temp.left = None
        temp.right = None
        temp.data = data


class Tree:

    def buildtree(self,root):
        arr=[]
        self.inorder(root,arr)
        print(arr)
        self.sortedarraytobalancedBST(arr,0,len(arr)-1)




    def sortedarraytobalancedBST(self,arr,start,end):

        if(start>end):
            return None
        mid=(start+end)//2
        root=Node(arr[mid])

        root.left=self.sortedarraytobalancedBST(arr,start,mid-1)
        root.right=self.sortedarraytobalancedBST(arr,mid+1,end)

        return root

    def inorder(self,root,arr):
        if(root!=None):
            self.inorder(root.left,arr)
            arr.append(root.data)
            self.inorder(root.right,arr)

    def inorder1(self,root):
        if(root!=None):
            self.inorder1(root.left)
            print(root.data)
            self.inorder1(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

if __name__ == "__main__":
    fp = Tree()

    # for i in a:
    #     data = fp.insert(i)
    # print(data)

    data=fp.buildtree(root)
    print(data)
    fp.inorder1(data)

