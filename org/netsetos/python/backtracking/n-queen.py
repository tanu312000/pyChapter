class Nqueen:
    N=4
    def printSolution(self,board):
        size=len(board)
        for i in range(0,size):
            for j in range(0,size):
                print(board[i][j])

    def isSafe(self,board,row,col):
        for i in range(0,col):
            if(board[row[i]]==1):
                return False

        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if(board[i][j]==1):
                return False

        for i,j in zip(range(row,Nqueen.N,1),range(col,-1,-1)):
            if(board[i][j]==1):
                return False
        return False

    def Solve_N_Queen(self,board,col):
        if(col >= Nqueen.N):
            return True



        if(self.isSafe(board,col)):
            board[i][col]=1
