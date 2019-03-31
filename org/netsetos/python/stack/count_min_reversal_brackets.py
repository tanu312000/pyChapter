import math
class count_min_reversal:
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

    def count_min_reversal(self,arr):
        size=len(arr)
        if(size%2!=0):
            return -1
        for i in range(size):
            if(arr[i] == '}' and self.top!=-1):
                X=self.stack[self.top]
                if(X=='{'):
                    self.pop()
                else:
                    self.push(arr[i])
            else:
                self.push(arr[i])

        unbal_len=self.top
        print(self.top)
        n=0
        while(self.top!=-1 and self.stack[self.top]=='{'):
            self.pop()
            n=n+1
        return math.ceil(unbal_len/2 +n%2)

if __name__ == "__main__":
    fp = count_min_reversal()
    arr= ['}','}','{','{','}','}','{','{']
    data=fp.count_min_reversal(arr)
    print(data)
