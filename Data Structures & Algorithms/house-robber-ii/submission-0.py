class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_1(nums[1:]),
                   self.rob_1(nums[:-1]))
    
    def rob_1(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]