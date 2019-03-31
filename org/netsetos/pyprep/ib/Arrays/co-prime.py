class gcd:
    def co_prime(self,A,B):
        while(self.gcd(A,B)!=1):
            A=int(A/self.gcd(A,B))
        return A

    def gcd(self,A,B):
        while(A!=0):
            temp=B
            B=A
            A=int(temp%A)
        return B
obj=gcd()
prime=obj.co_prime(30,12)
print(prime)

