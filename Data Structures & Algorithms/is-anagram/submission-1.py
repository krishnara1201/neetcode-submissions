class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        set_1 = {}
        set_2 = {}

        for i in range(len(s)):
            set_1[s[i]] = set_1.get(s[i], 0) + 1
            set_2[t[i]] = set_2.get(t[i], 0) + 1
        
        return set_1 == set_2

             
        