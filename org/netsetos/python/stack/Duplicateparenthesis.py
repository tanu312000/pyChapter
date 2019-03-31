class Duplicateparenthesis:
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

    def Duplicateparenthesis(self,arr):
        size=len(arr)
        for i in range(size):
            if(arr[i]==')'):
                tp=self.stack[self.top]
                self.pop()
                element=0
                while (tp != '('):
                    element=element+1
                    tp = self.stack[self.top]
                    self.pop()
                if(element<=1):
                    return 1
            else:
                self.push(arr[i])
        return 0


if __name__ == "__main__":
    fp = Duplicateparenthesis()
    arr= "(a+b)"
    data=fp.Duplicateparenthesis(arr)
    print(data)
