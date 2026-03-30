class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack = []

        def dfs(i):
            nonlocal res
            if i > n + 1:
                return
            elif len(stack) == k:
                res.append(stack[::])
                return
            else:
                stack.append(i)
                dfs(i + 1)
                stack.pop()
                dfs(i + 1)
        
        dfs(1)
        return res
