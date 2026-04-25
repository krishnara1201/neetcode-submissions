class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alen, blen = len(s1), len(s2)
        if (alen > blen):
            return False
        
        for i in range(alen-1, blen):
            if self.is_anagram(s1, s2[i-alen+1:i+1]):
                return True
        return False
        
    def is_anagram(self, a,b):
        dic_a = [0] * 26
        dic_b = [0] * 26
        for i in range(len(a)):
            dic_a[ord(a[i])-ord('a')] += 1
            dic_b[ord(b[i])-ord('a')] += 1
        
        return dic_a == dic_b