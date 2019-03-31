from collections import OrderedDict
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def buildHashTable(root,max,min,hd,dict):
    if(root!=None):
        if(dict.get(hd) !=None):
            dict[hd].append(root.data)
        else:
            dict[hd]=[root.data]
        if (hd < min[0]):
            min[0] = hd
        elif (hd > max[0]):
            max[0] = hd

        buildHashTable(root.left, max, min, hd - 1,dict)
        buildHashTable(root.right,max, min, hd + 1,dict)





root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("d")
root.left.right = Node("e")
root.right.left = Node("f")
root.right.right = Node("g")
root.left.left.left = Node("h")
root.left.left.right = Node("i")
root.left.left.right.left = Node("m")
root.left.left.right.right = Node("n")
root.right.left.left = Node("j")
root.right.left.right = Node("k")
root.right.left.right.left = Node("p")
root.right.left.right.right = Node("q")
root.right.right.right = Node("l")



min=[0]
max=[0]
hd=0
dict={}

data=buildHashTable(root,min,max,hd,dict)
print(min)
print(max)
print(dict)
m= OrderedDict(sorted(dict.items()))
od=list(m.values())
print(od)

