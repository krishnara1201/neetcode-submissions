class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        # [1, 2, 3, 4, 5] -> [1,3], [1,4], [2,4], [2,5], [3,5]
        return max(self.rob_1(nums[1:n]), self.rob_1(nums[:n-1]))

    def rob_1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]
