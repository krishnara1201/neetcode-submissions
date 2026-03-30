class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        visit = set()
        def bfs(row,col):
            q = deque()
            q.append([row, col])
            visit.add((row,col))
            res = 1
            while q:
                r,c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == 0:
                        continue
                    visit.add((nr,nc))
                    q.append([nr,nc])
                    res += 1
            
            return res
        
        area = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))

        return area
            
