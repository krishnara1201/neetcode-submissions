class Solution:
    def isValid(self, s: str) -> bool:
        close_dic = {"}":"{" , "]":"[" , ")":"("}
        stack = []
        for c in s:
            if c in close_dic:
                if stack and stack[-1] == close_dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        return True