class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        
        character_set = set()
        max_sub = 0
        for r in range(n):
            if s[r] in character_set:
                while s[l] != s[r] and l < r:
                    character_set.remove(s[l])
                    l += 1
                l += 1
            else:
                character_set.add(s[r])
            
            print(character_set)
            max_sub = max(max_sub, r - l + 1)
        
        return max_sub

            