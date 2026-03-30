class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def dfs(i, cur, total):
            if len(cur) == 4 and total == target:
                res.append(cur.copy())
                return 
            if (len(cur) >= 4 and total != target) or i >= n:
                return
            
            cur.append(nums[i])
            dfs(i+1, cur, total + nums[i])
            cur.pop()
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur, total)
    
        dfs(0, [], 0)

        return res