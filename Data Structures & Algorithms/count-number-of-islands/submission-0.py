class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowl, coll = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        islands = 0

        visited = set()
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nr >= rowl or nc < 0 or nc >= coll or (nr, nc) in visited or grid[nr][nc] == "0":
                        continue
                    
                    visited.add((nr,nc))
                    q.append((nr,nc))

        for c in range(coll):
            for r in range(rowl):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands