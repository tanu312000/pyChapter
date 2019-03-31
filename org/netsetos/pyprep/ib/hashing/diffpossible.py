def diffPossible( A, B):
    d = set()
    for i in range(len(A)):
        if (A[i] - B in d or A[i] + B in d):
            return 1
        else:
            d.add(A[i])
    return 0

A=[ 11, 85, 100, 44, 3, 32, 96, 72, 93, 76, 67, 93, 63, 5, 10, 45, 99, 35, 13 ]
B=60
test=diffPossible(A, B)
print(test)