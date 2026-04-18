class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        visit = set()
        heap = [(0,0,0)]
        
        while heap:
            e,r,c = heapq.heappop(heap)
            if (r,c) in visit:
                continue
            if (r,c) == (ROWS-1, COLS-1):
                return e
            visit.add((r,c))
            min_effort = 1000000

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 
                    0 <= nc < COLS and
                    (nr,nc) not in visit):
                    effort = max(e, abs(heights[nr][nc] - heights[r][c]))
                    heapq.heappush(heap, (effort,nr,nc))
            
        return 0