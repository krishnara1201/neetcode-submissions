class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        

        def dfs(r,c, dist):
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            (r,c) in visited or 
            grid[r][c] == -1):
                return
            else:
                visited.add((r,c))
                grid[r][c] = min(grid[r][c], dist)
                dfs(r+1,c,dist+1)
                dfs(r,c+1,dist+1)
                dfs(r-1,c,dist+1)
                dfs(r,c-1,dist+1)
                return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited = set()
                    dfs(r,c,0)

        return 
