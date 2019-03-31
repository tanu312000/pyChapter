class Evaluate_Span:
    def __init__(self):
        self.top = -1
        self.maxsize=10
        self.stack=[0]*self.maxsize




    def push(self,data):
        if(self.top == self.maxsize-1):
            print("Overflow")
        else:
            self.top=self.top+1
            self.stack[self.top]=data
            #print("Value added in stack",data)

    def pop(self):
        temp=-1
        if(self.top == -1):
            print("Underflow")
        else:
            temp=self.stack[self.top]
            self.top=self.top - 1
        return temp

    def evaluatespan(self):
        price=[100,30,10,20,25,40,26,35,45]
        size=len(price)
        self.push(0)
        self.span = [0] * len(price)
        self.span[0]=0

        for i in range(1,size):
            while(self.top!=-1 and price[self.stack[self.top]] <= price[i]):
                self.pop()
            if(self.top == -1):
                self.span[i]=i
            else:
                self.span[i] = i -self.stack[self.top] - 1
            self.push(i)
        return self.span

if __name__ == "__main__":
    fp = Evaluate_Span()
    arr=[34,35,27,42,5,28,39,20,28]
    data=fp.evaluatespan()

    print(data)
