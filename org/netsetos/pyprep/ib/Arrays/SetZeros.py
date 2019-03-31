def SetZeros(mat):
    firstRowHasZeros=False
    firstColHasZeros=False

    #Check if first column has any zeroes
    for i in range(0,len(mat)):
        if(mat[i][0] ==0):
            firstColHasZeros = True

    # Check if first row has any zeroes
    for i in range(0,len(mat[0])):
        if(mat[0][i] ==0):
            firstRowHasZeros = True

    #Check rest of matrix for zeros,mark the row and column using first row and column
    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if(mat[i][j] ==0):
                mat[0][j]=0
                mat[i][0]=0

    #Zerofy the marked Columns and Rows
    for i in range(1,len(mat)):
        if(mat[i][0]==0):
            for j in range(1,len(mat[0])):
                mat[i][j]=0

    for i in range(1,len(mat[0])):
        if(mat[0][i]==0):
            for j in range(1,len(mat)):
                mat[j][i]=0

        # Zerofy first Column and Row if necessary
    if firstRowHasZeros:
        for i in range(0, len(mat[0])):
            mat[0][i] = 0

    if firstColHasZeros:
        for i in range(0, len(mat)):
            mat[i][0] = 0

    return mat


mat=[[1,1,1,1],
     [0,1,1,1],
     [1,1,1,1]]
d=SetZeros(mat)
print(d)



