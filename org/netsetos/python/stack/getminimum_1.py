class Node:     #Stackimplement_using_arr
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.stack1=[0]*maxsize
        self.top1=-1
        self.stack2 = [0]*maxsize
        self.top2 = -1

    def push(self, data):
        if (self.top1 == self.maxsize - 1):
            print("Overflow")
        else:
            self.top1= self.top1 + 1
            self.stack1[self.top1] = data
            print("Value added in stack", data)


            if (self.top2==-1 or self.stack1[self.top1] <= self.stack2[self.top2]):
                self.top2 = self.top2 + 1
                self.stack2[self.top2] = data
            # else:
            #     temp = self.stack2[self.top2]
            #     self.top2 = self.top2 + 1
            #     self.stack2[self.top2] = temp

    def pop(self):
        temp = -1
        if (self.top1 == -1):
            print("Underflow")
        else:
            temp = self.stack1[self.top1]
            self.top1 = self.top1 - 1
            if(self.stack1[self.top1]==self.stack2[self.top2]):
                temp = self.stack2[self.top2]
                self.top2 = self.top2 - 1


        return temp

    def getminimum(self,data):
        print("Minimum element is",self.stack2[self.top2])
        print(self.stack2)







if __name__ == "__main__":
    fp = Node(5)
    fp.push(1)
    fp.push(13)
    fp.push(20)
    fp.push(15)
    fp.push(9)
    fp.push(5)
    fp.pop()
    fp.getminimum(5)




