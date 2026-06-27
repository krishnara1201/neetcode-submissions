class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * COLS for _ in range(ROWS)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if obstacleGrid[r][c] == 0 and (r,c) !=(0,0):
                    if (r == 0):
                        dp[r][c] = dp[r][c-1]
                    elif (c == 0):
                        dp[r][c] = dp[r-1][c]
                    else:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[ROWS-1][COLS-1]