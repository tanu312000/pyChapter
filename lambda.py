def maxp3( A):
    size=len(A)
    A.sort()
    print(A)
    for i in range(size):
        twonegative = A[0] * A[1] * A[size - 1]
        print(twonegative)
        allpositive = A[size - 3] * A[size - 2] * A[size - 1]
        print(allpositive)



    if(twonegative>allpositive):
        print('--',twonegative)
    else:
        print('--oo',allpositive)






A=[ 1, 3, 5, 2, 8, 0, -1, -3 ]
maxp3(A)