def add_binary(A,B):
    a=int(A,2)
    b=int(B,2)
    c=bin(a+b)[2:]
    return c

A="100"
B="11"
d=add_binary(A,B)
print(d)