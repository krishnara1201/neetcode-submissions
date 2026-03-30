class Solution:
    def isValid(self, s: str) -> bool:
        closed_dic = {")":"(",
        "]":"[",
        "}":"{"}

        stack = []

        for i in s:
            if i not in closed_dic:
                stack.append(i)
            elif not stack or stack[-1] != closed_dic[i]:
                    return False
            else: 
                stack.pop()

        return False if stack else True