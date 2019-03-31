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

    def printing_right(self,arr):
        size=len(arr)
        output= [-1] * size
        self.top=-1
        output[0]=self.push(arr[0])
        for i in range (1,size):
            next=arr[i]
            if(self.top!=-1):
                element=self.pop()
                while(next>element):
                    print('element--',element,'next--',next)
                    if(self.top==-1):
                        break
                    element=self.pop()
                if(next<element):
                    self.push(element)
                self.push(next)
        while(self.top!=-1):
            element=self.pop()
            next=-1
            print('element--', element, 'next--', next)

if __name__ == "__main__":
    fp = Reversal()
    arr=[10,12,7,9,6,89]
    fp.printing_right(arr)

