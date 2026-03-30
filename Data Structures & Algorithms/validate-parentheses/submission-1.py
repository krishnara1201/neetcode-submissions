class Solution:
    def isValid(self, s: str) -> bool:
        closed_para = {")":"(","]":"[","}":"{" }
        stack = []

        for i in s:
            if i in closed_para:
                if stack and stack[-1] == closed_para[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if stack:
            return False
        return True