class Queue:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.arr=[0]*1

    def Enqueue(self,data):

        self.size=len(self.arr)
        # self.front=-1
        # self.rear=-1
        if((self.rear+1)%self.size==self.front):
            print("Queue is full")
        elif (self.front==-1 and self.rear==-1):
            self.front=0
            self.rear=0
            self.arr[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.arr[self.rear]=data
        print(self.arr[self.rear])

    def Dequeue(self):
        if(self.front==-1 and self.rear==-1):
            print("Underflow")
        elif(self.front==self.rear):
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.size

        print(self.arr[self.rear])

if __name__ == "__main__":
    fp = Queue()
    fp.Enqueue(10)
    fp.Enqueue(20)
    # fp.Enqueue(30)
    # fp.Enqueue(40)
    # fp.Dequeue()