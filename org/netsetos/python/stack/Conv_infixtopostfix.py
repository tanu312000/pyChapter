class Conversion:
    def __init__(self,size):
        self.top=-1
        self.size=size
        self.stack=[]
        self.output=[]
        self.precedance={'+':1,'-':1,'*':2,'/':2,'^':3}


    def isEmpty(self):
        if(self.top==-1):
            return True
        else:
            return False

    def peek(self):
        return self.stack[self.top]

    def pop(self):
        if(self.isEmpty()==True):
            print("Underflow")
        else:
            temp=self.stack[self.top]
            self.top=self.top-1
            return temp

    def push(self,data):
        if(self.top==self.size-1):
            print("Overflow")
        else:
            self.top=self.top+1
            self.stack.append(data)

    def isoperand(self,ch):
        return ch.isalpha()

    def CheckGreator(self,i):#i is defined as expression
        try:
            a=self.precedance[i]
            b=self.precedance[self.stack.top]
            if(a<=b):
                return True
            else:
                return False
        except KeyError:
            return False

    def infix_to_Postfix(self,exp):
        for i in exp:
            if(self.isoperand(i)):
                self.output.append(i)
            elif(i=='('):
                self.push(i)
            elif(i==')'):
                while(self.top!=-1 and self.stack.top!='('):
                    a=self.pop()
                    self.output.append(a)
                if(self.top!=-1 and self.stack.top!='('):
                    return -1
                else:
                    self.pop()
            else:      #if it is a operator
                while(self.top!=-1 and self.checkGreater(i)):
                    a=self.pop()
                    self.output.append(a)
            self.push(i)

            while(self.top!=-1):
                b=self.pop()
                self.output.append(b)
            print(self.output)

if __name__ == "__main__":
    exp="a*b+(c-d)"
    fp = Conversion(len(exp))
    fp.infix_to_Postfix(exp)



