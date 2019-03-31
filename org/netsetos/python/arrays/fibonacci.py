def fibonacci(n):
    a=0
    b=1
    if(n<0):
        print("Incorrect Input")
    elif(n==0):
        return a
    elif(n==1):
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b

def fibonacci1(n):
    if(n<0):
        print("Incorrect Input")
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacci1(n-1)+fibonacci1(n-2)

d=fibonacci1(9)
print(d)

