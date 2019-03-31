def count (A):
    i = 5
    zeros = 0
    while (A >= i):
        zeros=zeros+ A // i
        i =i* 5
    return zeros


n=100
d=count(n)
print(d)