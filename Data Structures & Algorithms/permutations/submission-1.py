class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        def dfs(stack, pick):
            if len(stack) == n:
                res.append(stack.copy())
                return
            else:
                for i in range(n):
                    if not pick[i]:
                        stack.append(nums[i])
                        pick[i] = True
                        dfs(stack, pick)
                        stack.pop()
                        pick[i] = False
                
        dfs([], [False] * n)

        return res