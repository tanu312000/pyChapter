class Node:

    def __init__(temp, data):
        temp.left = None
        temp.right = None
        temp.data = data


class Tree:

    def levelordertraverse(self,root):
        queue=[]
        queue.append(root)

        while(len(queue)>0):
            front=queue[0].data
            print(front)
            current=queue.pop(0)
            if(current.left!=None):
              queue.append(current.left)
            if(current.right!=None):
              queue.append(current.right)



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

    data=fp.levelordertraverse(root)
    print(data)
