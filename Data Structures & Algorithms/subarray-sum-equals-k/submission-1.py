class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        def dfs(cur_sum, i):
            nonlocal res
            
            if i >= len(nums):
                return
            
            if cur_sum == k:
                res += 1
            
            dfs(cur_sum + nums[i], i + 1)
            dfs(cur_sum, i + 1)
        
        dfs(0,0)

        return res