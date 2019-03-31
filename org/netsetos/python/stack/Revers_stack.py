class Reversal:
    def __init__(self):

        self.maxsize = 10
        self.stack = [0] * self.maxsize
        self.top = -1

    def push(self,data):
        if(self.top == self.maxsize-1):
            print("Overflow")
        else:
            self.top=self.top+1
            self.stack[self.top]=data
            print("Value added in stack",data)

    def pop(self):
        temp=-1
        if(self.top == -1):
            print("Underflow")
        else:
            temp=self.stack[self.top]
            self.top=self.top - 1
            return temp

    def Insert_at_Bottom(self,item):
        if(self.top==-1):
            self.push(item)

        else:
            topitem=self.pop()
            self.Insert_at_Bottom(item)
            self.push(topitem)

    def reverse(self):
        if (self.top) != -1:
            item=self.pop()
            self.reverse()
            self.Insert_at_Bottom(item)
        print(self.stack)

    # def isEmpty(self):
    #     if(self.top)==-1:
    #         return True
    #     else:
    #         return False

if __name__ == "__main__":
    fp = Reversal()
    fp.push(10)
    fp.push(20)
    fp.push(30)
    fp.push(5)
    fp.reverse()
    print(fp.stack)



