class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        n = len(nums)
        
        def dfs(i, stack):
            if i == n:
                res.append(stack.copy())

            else:
                stack.append(nums[i])
                dfs(i + 1, stack)
                stack.pop()
                dfs(i + 1, stack)
        
        dfs(0, stack)
        return res