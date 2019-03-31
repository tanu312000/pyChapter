def reverse_col(arr,Row,Col):
    for i in range(0,Row):
        j = 0
        k = Col - 1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j =j+1
            k = k-1

def transpose(arr,Rows,Col):
    for i in range(0,Rows):
        for j in range(i,Col):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

def rotate90(matrix,row,col):
    transpose(matrix,row,col)
    reverse_col(matrix,row,col)

# Function for print matrix
def printMatrix(arr):
    for i in range(4):
        for j in range(4):
            print(str(arr[i][j]), end =" ")
        print()


matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]
        ]




matrix=rotate90(matrix,4,4)
printMatrix(matrix)
