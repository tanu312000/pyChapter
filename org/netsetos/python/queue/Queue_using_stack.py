class Stack_arr:     #Stackimplement_using_arr
    def __init__(self,maxsize):
        self.maxsize=8
        self.stack1=[0] * maxsize
        self.stack2 = [0] * maxsize
        self.top1=-1
        self.top2= -1

    def insert(self, data):
        stack = self.stack1

        if(self.top1==self.maxsize -1 ):
            print("Overflow")

        else:
            self.top1=self.top1+1
            stack[self.top1]=data
        print('[insert]',stack[self.top1])

    def delete(self):
        stack1=self.stack1
        stack2 = self.stack2
        if(self.top2==-1):
            if(self.top1==-1):
                print("Underflow")
            else:
                while(self.top1!=-1):
                    temp=self.stack1[self.top1]
                    self.top1=self.top1-1
                    self.top2 = self.top2 - 1
                    self.stack2[self.top2]=temp
                    print('deleted-',self.stack2[self.top2])

        temp = self.stack2[self.top2]
        print('[deleted]-2', self.stack2[self.top2])
        self.top2 = self.top2 - 1











if __name__ == "__main__":
    fp = Stack_arr(10)
    fp.insert(10)
    fp.insert(20)
    fp.insert(30)
    fp.insert(40)
    fp.insert(50)
    fp.delete()

