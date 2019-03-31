def Single_one(A):
    ones=0
    twos=0

    n=len(A)
    for i in range(0,n):
        twos=twos|(ones & A[i])
        ones=ones^A[i]
        not_threes = ~(ones & twos)
        ones=ones & not_threes
        twos=twos & not_threes


    return ones


A=[3,3,2,3]
d=Single_one(A)
print(d)

