def HCF(A,B):
    while(A!=0):
        temp=B
        B=A
        A=temp%A
    print(A,B)
    print(20%10)
    return B






HCF(10,20)