class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        res = 0
        visit = set()

        def dfs(r, c):
            nonlocal res
            
            if (r,c) in visit or grid[r][c] != 1:
                return
            visit.add((r,c))
            


            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 
                    0 <= nc < COLS and
                    grid[nr][nc] == 1):
                    dfs(nr, nc)
                else:
                    res += 1
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)

        return res