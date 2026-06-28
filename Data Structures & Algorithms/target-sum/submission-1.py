class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        def dfs(i, cur_sum):
            nonlocal count
            if i == n:
                if cur_sum == target:
                    count += 1
                return

            dfs(i+1, cur_sum + nums[i])
            dfs(i+1, cur_sum - nums[i])

        dfs(0,0)
        return count