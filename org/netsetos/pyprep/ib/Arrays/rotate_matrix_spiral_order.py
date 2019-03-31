def spiralPrint(A) :
    m=len(A)
    n=len(A[0])
    Top=0
    Bottom=m-1
    left=0
    Right=n-1
    dir=0
    res=[]

    while(Top<=Bottom and left<=Right):
        if(dir == 0):
            for i in range(left,Right+1):
                res.append(A[Top][i])
            Top=Top+1
            dir=1

        elif(dir == 1):
            for i in range(Top,Bottom+1):
                res.append(A[i][Right])
            Right=Right-1
            dir=2

        elif(dir==2):
            for i in range(Right,left+1):
                res.append(A[Bottom][i])
            Bottom=Bottom-1
            dir=3

        else:
            for i in range(Bottom,Top+1):
                res.append(A[i][left])
            left=left+1
            dir=0
    return res

A=[[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
d=spiralPrint(A)
print(d)