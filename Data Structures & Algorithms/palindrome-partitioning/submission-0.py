class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def dfs(i, stack):
            if i >= n:
                res.append(stack.copy())
                return
            
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    stack.append(s[i:j+1])
                    dfs(j + 1, stack)
                    stack.pop()
        
        dfs(0,[])
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

        