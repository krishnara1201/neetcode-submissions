class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif i == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif i == "-":
                temp = stack.pop()
                val = stack.pop() - temp
                stack.append(val)
            elif i == "/":
                temp = stack.pop()
                val = int(stack.pop()//temp)
            else:
                stack.append(int(i))
        
        return stack.pop()