class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def findMinMax(root, min, max, hd):
    if (root == None):
        return 0


    if (hd < min[0]):
        min[0] = hd
    elif (hd > max[0]):
        max[0] = hd


    findMinMax(root.left, min, max, hd - 1)
    findMinMax(root.right, min, max, hd + 1)


def printVerticalLine(root, line_no, hd):
    if (root == None):
        return 0

    if (hd == line_no):
        print(root.data)

    printVerticalLine(root.left, line_no, hd - 1)
    printVerticalLine(root.right, line_no, hd + 1)


def verticalOrder(root):

    minimum = [0]
    maximum = [0]
    findMinMax(root, minimum, maximum, 0)

    for line_no in range(minimum[0], maximum[0] + 1):
        printVerticalLine(root, line_no, 0)

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

print("Vertical order traversal is",verticalOrder(root))
