def f1(a,b):
    sum_ab=a+b
    sub_ab=a-b
    mul_ab=a*b
    div_ab=a//b

    return sum_ab,sub_ab,mul_ab,div_ab

x=f1(200,100)
print(type(x))
print(x)