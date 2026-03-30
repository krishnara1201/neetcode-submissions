class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[n-1]
        dp[1] = cost[n-2]
        for i in range(2,n):
            dp[i] = min(dp[i-1] + cost[n-1-i], dp[i-2] + cost[n-1-i])
        print(dp)
        return min(dp[n-1], dp[n-2])
            