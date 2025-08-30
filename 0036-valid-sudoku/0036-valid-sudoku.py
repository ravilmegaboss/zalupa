class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        for box in range(9):
            seen = set()
            start_i = (box // 3) * 3
            start_j = (box % 3) * 3
            for i in range(start_i, start_i + 3):
                for j in range(start_j, start_j + 3):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        
        return True