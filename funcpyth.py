def  outer():
    def inner(a,b):
        print("The sum is ",a+b)
        print("The product is ", a*b)
    inner(1,2)
    return inner
    inner(10, 20)


outer()