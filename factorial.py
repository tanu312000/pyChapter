def fact(n):
    if n==0 :
        return 1
    else:
        r=n*fact(n-1)

    return r

#5*fact(4)
#5*4*fact(3)

print(fact(5))