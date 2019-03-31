class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def EnQueue(self,data):
        if(self.rear== None):
            self.rear=Node(data)
            self.front=self.rear
        else:
            newNode=Node(data)
            self.rear.next=newNode
            self.rear=newNode

    def DeQueue(self):
        if(self.front== None):
            return

        else:
            temp=self.front
            self.front = temp.next

            if (self.front == None):
                self.rear = None
            return str(temp.data)















if __name__ == "__main__":
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
    q.EnQueue(10)
    q.EnQueue(20)
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)



    data=q.DeQueue()
    print(data)

