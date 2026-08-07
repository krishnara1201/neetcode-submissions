class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i in ["1","2","5"]:
                stack.append(int(i))
            elif stack:
                if i == "+":
                    stack.append(stack[-1] + stack[-2])
                elif i == "C":
                    stack.pop()
                elif i == "*":
                    stack.append(stack[-1] * stack[-2])
                else:
                    stack.append(stack[-1] * 2)
        
        return sum(stack)