def NumSetBits(A):
    s=0
    while(A!=0):
        rem=A%2
        s=s+rem
        A=A/2
    return s

test=NumSetBits(3)
print(test)