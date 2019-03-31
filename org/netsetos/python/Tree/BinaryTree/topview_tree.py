from collections import OrderedDict
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def buildHashTable(self,root, max, min, hd, dict):
        if (root != None):
            if (dict.get(hd) != None):
                print(dict.get(hd))
            else:
                dict[hd] = [root.data]

                if (hd < min[0]):
                    min[0] = hd
                elif (hd > max[0]):
                    max[0] = hd


            self.buildHashTable(root.left, max, min, hd - 1, dict)
            self.buildHashTable(root.right, max, min, hd + 1, dict)


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')


if __name__ == "__main__":
    min = [0]
    max = [0]
    hd = 0
    dict = {}
    
    fp=Tree()

    data = fp.buildHashTable(root, min, max, hd, dict)
    print(min)
    print(max)
    print(dict)
    m = OrderedDict(sorted(dict.items()))
    od = list(m.values())
    print(od)
