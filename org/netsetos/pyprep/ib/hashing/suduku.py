def isValidSudoku(A):
    rowD = [{} for i in range(9)]
    colD = [{} for i in range(9)]
    boxD = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            ele = A[i][j]
            if ele != '.':
                if A[i][j] not in rowD[i]:
                    rowD[i][A[i][j]] = 1
                else:
                    return 0
                if A[i][j] not in colD[j]:
                    colD[j][A[i][j]] = 1
                else:
                    return 0
                # boxNumber =int( 3 * int(i / 3) + int(j / 3))
                boxNumber = (3 * int(i / 3) + int(j / 3))
                # print(boxNumber)
                if ele not in boxD[boxNumber]:
                    boxD[boxNumber][ele] = 1
                else:
                    return 0

    return 1

A=["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
test=isValidSudoku(A)
print(test)