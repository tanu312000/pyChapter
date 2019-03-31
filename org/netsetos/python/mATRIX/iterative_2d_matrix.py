class matrix:
    def matrix_chain(self, p, n):
        matrix = [[0 for x in range(p)] for y in range(n)]

        print(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(i==0 or i==2):
                    matrix[i][j]=1
                print(matrix[i][j],end='')
            print()



t = matrix()
t.matrix_chain(8, 5)