def HCF(x,y):
    if x>y:
        larger=x
    else:
        larger=y
    for i in range(1,larger+1):
        if((x%i==0) or (y%i==0)):
            hcf=i

    return hcf
print(HCF(18,24))

HCF(18,24)











