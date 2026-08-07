class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = set("zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890")

        l = 0
        r = len(s) - 1
        
        while l < r:
            while s[l] not in alpha:
                l += 1
            while s[r] not in alpha:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        
        return True