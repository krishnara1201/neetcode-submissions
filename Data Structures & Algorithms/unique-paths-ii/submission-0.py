class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[1] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if not(r == 0 or c == 0):
                    if obstacleGrid[r][c] == 1:
                        dp[r][c] = 0
                    else:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[ROWS-1][COLS-1]