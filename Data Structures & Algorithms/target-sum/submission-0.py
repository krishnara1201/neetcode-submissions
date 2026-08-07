class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp = [[0]*len(nums) for _ in range(2)]
        count = 0
        n = len(nums)
        def dfs(i, cur_sum):
            if i >= n:
                if cur_sum == target:
                    count += 1
                return

            dfs(i+1, cur_sum + nums[i])
            dfs(i+1, cur_sum - nums[i])
        dfs(0,0)
        return count