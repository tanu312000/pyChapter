class Reversal:
    def __init__(self):

        self.maxsize = 10
        self.stack = [0] * self.maxsize
        self.top = -1
        self.arr2 = [-1] * 6


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

    def prevSmaller(self, A):
        size = len(A)
        #stack = []

        output = [-1] * size

        for i in range(0, size):
            if (self.top!= -1):
                while (self.stack[self.top] >= A[i]):
                    self.pop()

            if (self.top == -1):
                output[i] = -1

            else:

                output[i] = self.stack[self.top]


            self.push(A[i])
        return output

if __name__ == "__main__":
    fp = Reversal()
    arr=[ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
    data=fp.prevSmaller(arr)
    print(arr)
    print(data)

