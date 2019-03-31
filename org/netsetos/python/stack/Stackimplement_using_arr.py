class Stack_arr:     #Stackimplement_using_arr
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.stack=[0]*maxsize
        self.top=-1



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


if __name__ == "__main__":
    fp = Stack_arr(10)
    fp.push(10)
    fp.push(20)
    fp.push(30)
    fp.push(40)
    fp.push(50)
    fp.push(60)
    fp.push(70)
    fp.push(10)
    fp.push(20)
    fp.push(30)
    fp.push(40)
    fp.push(50)
    fp.push(60)
    fp.push(70)
    # fp.pop()

