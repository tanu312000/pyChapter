def rotate( A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    for i in A:
        i.reverse()

    return A

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
d=rotate(A)
print(d)