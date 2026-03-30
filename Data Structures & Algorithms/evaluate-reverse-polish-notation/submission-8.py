class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i == "+":
                add = res.pop() + res.pop()
                res.append(add)
            elif i == "-":
                sub = - res.pop() + res.pop()
                res.append(sub)
            elif i == "*":
                mult = res.pop() * res.pop()
                res.append(mult)
            elif i == "/":
                div = (1/res.pop()) * res.pop()
                res.append(int(div))
            else:
                res.append(int(i))
        
        return int(res.pop())
