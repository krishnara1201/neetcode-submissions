class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        res.append(int(tokens[0]))

        for i in tokens[1:]:
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
