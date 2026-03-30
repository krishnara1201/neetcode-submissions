class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        n = len(nums)

        def dfs(stack, i):
            if i >= n:
                res.append(stack.copy())
                return
            
            else:
                stack.append(nums[i])
                dfs(stack, i + 1)
                stack.pop()
                while i < n - 1 and nums[i] == nums[i+1]:
                    i += 1
                dfs(stack, i + 1)

        dfs([], 0)
        return res