class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def dfs(cur, pick):
            if len(cur) == n:
                res.append(cur.copy())
                return
            
            for i in range(n):
                if not pick[i]:
                    cur.append(nums[i])
                    pick[i] = True
                    dfs(cur, pick)
                    cur.pop()
                    pick[i] = False
        
        dfs([], [False] * n)
        return res