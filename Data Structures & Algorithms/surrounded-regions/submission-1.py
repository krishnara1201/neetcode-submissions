class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or 
            (r,c) in visit or
            board[r][c] != "O"):
                return 
            board[r][c] = "T"
            dfs(r,c)
            dfs(r,c)
            dfs(r,c)