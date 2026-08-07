class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if obstacleGrid[r][c] == 0:
                    if (r == 0 or c == 0):
                        dp[r][c] = 1
                    else:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]
        print(dp)
        return dp[ROWS-1][COLS-1]