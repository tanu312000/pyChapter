class Infix_To_Postfix:
    def __init__(self):
        self.top=-1
        self.capacity=20
        self.stack=[0] * 20
        self.output=[]
        self.precedence={'+':1,'-':1,'*':2,'/':2,'^':3}

    def isEmpty(self):
        if(self.top == -1):
            return True
        else:
            return False

    def peek(self):
        return self.stack[self.top]

    def pop(self):
        if(self.isEmpty() == True):
            print("underflow")
        else:
            temp=self.stack[self.top]
            self.top=self.top-1
            return temp

    def push(self,data):
        if(self.top==self.capacity):
            print('overflow')
        else:
            self.top=self.top+1
            # self.stack.append(data)
            self.stack[self.top] = data

        # A utility function to check is the given character
        # is operand
    def isOperand(self, ch):
        return ch.isalpha()

    def checkGreater(self,operator):
        try:
            a=self.precedence[operator]
            b=self.precedence[self.stack[self.top]]
            if(a<=b):
                return True
            else:
                return False
        except KeyError:
            return False

    def infixToPostfix(self,exp):
        count=0
        for i in exp:
            count=count+1
            if(self.isOperand(i)):
                self.output.append(i)
            elif(i=='('):
                self.push(i)
            elif(i==')'):
                while(self.top != -1 and self.top != '('):
                    a=self.pop()
                    self.output.append(a)
                if(self.top != -1 and self.top != ')'):
                    return -1
                else:
                    self.pop()
            else:
                while(self.top != -1 and self.checkGreater(i)):
                    a=self.pop()
                    self.output.append(a)
                self.push(i)

        while(self.top != -1):
            self.output.append(self.pop())
        print('output',self.output)

exp = "a*b+(c-d)"
obj = Infix_To_Postfix()
obj.infixToPostfix(exp)