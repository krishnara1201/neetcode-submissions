class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2:
            return False

        target = total_sum // 2
        n = len(nums)

        # def dfs(i, cur_sum):
        #     if i >= n :
        #         return cur_sum == target:
                
        #     else:
        #         return dfs(i + 1, cur_sum) or dfs(i + 1, cur_sum + nums[i])

        # return dfs(0,0)

        # dp = [False] * (target + 1)
        # dp[target] = True

        # for j in range(target, -1, -1):
        #     for num in nums:
        #         dp[j] = dp[j] or dp[j + num]
        #     print(dp)
        
        
        # return dp[0]

        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

                

