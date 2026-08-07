class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0], [0,-1]]
        n = len(word)

        seen = set()

        def dfs(r,c,i):
            if i == n :
                return True
            elif (r,c) in seen:
                return False
            elif board[r][c] == word[i]:
                seen.add((r,c))
                ret = False
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        ret = ret or dfs(nr, nc, i + 1)

                seen.remove((r,c))
                return ret
            else:
                return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False