class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        n = len(s)

        if k == n:
            return n
        
        l = 0
        res = 0

        for r in range(n):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(count.values())
            
            while (r - l + 1) > maxf + k and l <= r:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
