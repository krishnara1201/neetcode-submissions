class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []

        def dfs(i, cur, total):
            if len(cur) == 3 and total == 0:
                res.append(cur.copy())
                return 
            if (len(cur) >= 3 and total != 0) or i >= n:
                return
            
            cur.append(nums[i])
            dfs(i+1, cur, total + nums[i])
            cur.pop()
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur, total)
    
        dfs(0, [], 0)

        return res