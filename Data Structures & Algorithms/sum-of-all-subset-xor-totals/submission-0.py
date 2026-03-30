class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        stack = []
        def dfs(i):
            nonlocal res
            if i == len(nums):
                if not stack:
                    return
                xor_sum = 0
                for i in stack:
                    xor_sum ^= i
                res += xor_sum
            else:
                stack.append(nums[i])
                dfs(i + 1)
                stack.pop()
                dfs(i + 1)
        
        dfs(0)
        return res
            
                
