class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        minute = 0
        while q and fresh > 0:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    q.append([nr,nc])
                    fresh -= 1
                    grid[nr][nc] = 2
                print(r,c)

            minute += 1
        
        return minute if fresh == 0 else -1