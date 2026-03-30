class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        # def dfs(open_par, closed_par, stack):
        #     if open_par == n:
        #         if closed_par == open_par:
        #             res.append("".join(stack))
        #         else:
        #             stack.append(")")
                
        #     else:
        #         stack.append("(")
        #         dfs(open_par + 1, stack)
        #         stack.pop()
        
        def dfs(open_par, closed_par):
            if open_par < n:
                if open_par > closed_par:
                    stack.append(")")
                    dfs(open_par, closed_par + 1)
                    stack.pop()
                stack.append("(")
                dfs(open_par + 1, closed_par)
                stack.pop()
            else:
                if closed_par == open_par:
                    res.append("".join(stack))
                else:
                    stack.append(")")
                    dfs(open_par, closed_par + 1)
                    stack.pop()
        
        dfs(0, 0)

        return res


