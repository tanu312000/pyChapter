class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def distancekfromleaf(treeNode, visited, pathlen, path, k):
    if (treeNode != None):
        path[pathlen] = treeNode.data
        visited[pathlen] = False
        if (treeNode.left == None and treeNode.right == None and (pathlen - k > 0) and visited[pathlen - k] == False):
            print(path[pathlen - k])
            visited[pathlen - k] = True
        distancekfromleaf(treeNode.left, visited, pathlen+1, path, k)
        distancekfromleaf(treeNode.right, visited, pathlen+1, path, k)




if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    root.left.right = Node(6)
    root.left.left.right = Node(5)
    root.right = Node(7)
    root.right.left = Node(8)
    root.right.left.right = Node(10)
    root.right.left.left = Node(9)

    path=[0]*20
    visited=[0]*20
    distancekfromleaf(root,visited,1,path,2)













