class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        steps = 0
        while q:
            qlen = len(q)
            
            for i in range(qlen):
                r, c = q.popleft()
                
                grid[r][c] = min(grid[r][c], steps)
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr in range(ROWS) and nc in range(COLS)
                    and grid[nr][nc] == INF):
                        q.append((nr,nc))
            steps += 1

