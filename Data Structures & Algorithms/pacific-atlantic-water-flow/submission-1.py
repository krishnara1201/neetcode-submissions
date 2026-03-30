class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(ocean, r, c, prevHeight):
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            (r,c) in ocean or
            heights[r][c] < prevHeight):
                return
            
            ocean.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(ocean, nr, nc, heights[r][c])

        for i in range(ROWS):
            dfs(pacific, i,0,heights[i][0])
            dfs(atlantic, i,COLS - 1, heights[i][COLS - 1])

        for j in range(COLS):
            dfs(pacific, 0, j, heights[0][j])
            dfs(atlantic, ROWS - 1, j, heights[ROWS - 1][j])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
        