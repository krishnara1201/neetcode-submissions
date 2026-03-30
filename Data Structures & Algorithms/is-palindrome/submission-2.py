class Solution:
    def isPalindrome(self, s: str) -> bool:
        anset=set("zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890")

        l, r = 0, len(s) - 1
        
        while l < r:
            while (s[l] not in anset) and l < r:
                    l += 1
            while (s[r] not in anset) and l < r:
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
                
                