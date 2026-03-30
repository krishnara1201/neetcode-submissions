class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set("+-/*")
        n = len(tokens)
        
        stack = []
        res = 0
        for i in tokens:
            
            if i not in operators:
                stack.append(int(i))
            else:
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                elif i == "-":
                    res = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif i == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    res = int(float(stack[-2]) / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
        return stack.pop()
