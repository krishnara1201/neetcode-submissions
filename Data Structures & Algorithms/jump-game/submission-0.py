class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-1, -1,-1):
            for j in range(i, min(n, i + nums[i] + 1)):
                if dp[j]:
                    dp[i] = True
        print(dp)
        return dp[0]