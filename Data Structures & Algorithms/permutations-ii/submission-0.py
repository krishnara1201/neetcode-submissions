class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = collections.Counter(nums)
        n = len(nums)
        
        res = []
        stack = []
        def dfs():
            if len(stack) == n:
                res.append(stack.copy())
        
            for num in count:
                if count[num] > 0:
                    stack.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    stack.pop()
        
        dfs()
        return res