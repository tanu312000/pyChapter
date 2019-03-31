class prime:
    def checkprime(self,num):
        count=0
        for i in range(2,num):
            if(num%i==0):
                count=count+1

        if(count>=1):
            return False
        return True
    def primesum(self,A):
        result=[]
        for i in range(2,A):
            num1=self.checkprime(i)
            isprime=A-i
            num2 = self.checkprime(isprime)
            if(num1==True and num2==True):
                result.append(i)
                result.append(isprime)
                return result




obj=prime()
d=obj.primesum(10)
print(d)
# s=obj.checkprime(7)
# print(s)