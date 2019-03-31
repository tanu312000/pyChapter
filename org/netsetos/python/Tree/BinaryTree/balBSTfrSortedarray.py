class Node:

    def __init__(temp, data):
        temp.left = None
        temp.right = None
        temp.data = data


class Tree:


    def sortedarraytobalancedBST(self,arr,start,end):

        if(start>end):
            return None
        mid=(start+end)//2
        root=Node(arr[mid])

        root.left=self.sortedarraytobalancedBST(arr,start,mid-1)
        root.right=self.sortedarraytobalancedBST(arr,mid+1,end)

        return root
    def inorder(self,root):
        if(root!=None):

            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)





if __name__ == "__main__":
    fp = Tree()

    # for i in a:
    #     data = fp.insert(i)
    # print(data)
    arr=[10,20,30,40,50,60,70]

    data=fp.sortedarraytobalancedBST(arr,0,len(arr)-1)
    data1=fp.inorder(data)




