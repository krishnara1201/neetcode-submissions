class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        max_len = 0
        for r in range(len(s)):
            if s[r] in char_set:
                while s[l] != s[r]:
                    char_set.remove(s[l])
                    l += 1
                l += 1
            else:
                char_set.add(s[r])
                max_len = max(max_len, r-l+1)
        
        return max_len
