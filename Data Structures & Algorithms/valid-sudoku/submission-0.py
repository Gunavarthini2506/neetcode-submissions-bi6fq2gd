class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #col
        for i in range(len(board)):
            s=set()
            count=0
            for j in range(len(board[i])):
                if board[j][i] !=".":
                    s.add(board[j][i])
                    count += 1
            if count!=len(s):
                return False
    #row
        for i in range(len(board)):
            s=set()
            count=0
            for j in range(len(board[i])):
                if board[i][j] !=".":
                    s.add(board[i][j])
                    count += 1
            if count!=len(s):
                return False  
        #square        
        for square in range(len(board)):
            s=set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j 
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in s:
                        return False
                    else:
                        s.add(board[row][col])
        return True