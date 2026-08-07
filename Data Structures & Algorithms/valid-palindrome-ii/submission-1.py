class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 2:
            return True
        count = 1
        l, r = 0, n - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif count > 0 and l < r - 1:
                if s[l + 1] == s[r]:
                    l += 2
                    r -= 1
                    count -= 1
                elif s[l] == s[r-1]:
                    r -= 2
                    l += 1
                    count -= 1
                else:
                    return False
            else:
                return False
        
        return True