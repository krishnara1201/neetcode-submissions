class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0], [0,-1]]
        n = len(word)

        seen = set()

        def dfs(r,c,i):
            if i == n :
                return True
            elif (min(r, c) < 0 or
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r, c) in seen):
                return False
            else:
                seen.add((r,c))
                ret = False
                ret = (dfs(r + 1, c, i + 1) or
                        dfs(r, c + 1, i + 1) or
                        dfs(r - 1, c, i + 1) or
                        dfs(r, c-1, i + 1))
                seen.remove((r,c))
                return ret
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False