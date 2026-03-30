class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, stack, cur_sum):
            if cur_sum == target:
                res.append(stack.copy())
                return
            elif cur_sum > target or i == n:
                return
            else:
                stack.append(candidates[i])
                dfs(i + 1, stack, cur_sum + candidates[i])
                stack.pop()

                while i < n - 1 and candidates[i] == candidates[i+1]:
                    i += 1
                
                dfs(i + 1, stack, cur_sum)
            
        dfs(0, stack, 0)
        return res
                
