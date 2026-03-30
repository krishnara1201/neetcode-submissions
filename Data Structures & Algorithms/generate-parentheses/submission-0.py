class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openB, closeB):
            if openB == closeB == n:
                res.append("".join(stack))
            
            if openB < n:
                stack.append("(")
                backtrack(openB + 1, closeB)
                stack.pop()

            if closeB < openB:
                stack.append(")")
                backtrack(openB, 1 + closeB)
                stack.pop()
        
        backtrack(0,0)
        return res
