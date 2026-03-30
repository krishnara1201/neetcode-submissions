class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openB = closeB = 0
        lst = list(s)
        i = 0
        while i < len(lst):
            if lst[i] == "(":
                openB += 1
            if lst[i] == ")":
                if closeB >= openB:
                    lst.pop(i)
                    continue
                else:
                    closeB += 1
            i += 1
            
        diff = openB - closeB
        j = len(lst) - 1
        while diff > 0:
            if lst[j] == "(":
                lst.pop(j)
                diff -= 1
            j -= 1

        return "".join(lst)
