class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdic, coldic, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif (board[i][j] in rowdic[i] or 
                board[i][j] in coldic[j] or
                board[i][j] in squares[(i//3,j//3)]):
                    return False
                else:
                    rowdic[i].add(board[i][j])
                    coldic[j].add(board[i][j])
                    squares[(i//3, j//3)].add(board[i][j])
        
        return True