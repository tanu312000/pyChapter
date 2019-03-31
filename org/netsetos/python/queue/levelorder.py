class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if (self.rear == None):
            self.rear = Node(data)
            self.front = self.rear
        else:
            new_node = Node(data)
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if (self.front == None):
            return
        else:
            temp = self.front
            self.front = temp.next
        if (self.front == None):
            self.rear = None
        return str(temp.data)

    class TreeNode:

        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

    def levelordertraversal(self,root):
        if (root != None):
            q = Queue()

            self.enqueue(root.data)
            while (self.front != None and self.rear != None)):
                temp = self.dequeue()
                print(temp.data)
            if (temp.left != None):
                self.enqueue(temp.left.data)
            if (temp.right != None):
                self.enqueue(temp.right.data)

            if __name__ == '__main__':
                rear = Node(1)
                nodeB = Node(2)
                nodeC = Node(3)
                nodeD = Node(4)
                nodeE = Node(5)
                nodeF = Node(6)
                rear.next = nodeB
                nodeB.next = nodeC
                nodeC.next = nodeD
                nodeD.next = nodeE
                nodeE.next = nodeF
                q = Queue()
                q.enqueue('g')
                q.enqueue('h')
                q.dequeue()
                q.dequeue()
                q.enqueue('i')
                q.enqueue('j')
                q.enqueue('k')
                q.dequeue()
                print(data)

