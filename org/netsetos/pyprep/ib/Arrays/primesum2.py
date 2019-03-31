class prime:

    def primesum(self, A):
        result = []
        result1 = []
        result = self.listprime(A)
        size = len(result)
        for i in range(0, size):
            j = A - result[i]
            if (self.checkprime(j) == True):
                result1.append(result[i])
                result1.append(j)

                return result1


    def checkprime(self, num):
        count = 0
        for i in range(2, num):
            if (num % i == 0):
                count = count + 1

        if (count >= 1):
            return False
        return True





    def listprime(self,A):
        result=[]
        for num in range(2,A):
            prime=True
            for i in range(2,num):
                if(num%i==0):
                    prime=False
            if(prime):
                result.append(num)
        return result



obj=prime()
d=obj.primesum(1048574)
print(d)


