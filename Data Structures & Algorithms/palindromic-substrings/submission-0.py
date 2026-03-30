class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for c in range(n):
            l,r = c, c 
            while (0 <= l < n and 0 <= r < n and
                    s[l] == s[r]):
                count += 1
                l -= 1
                r += 1

            l,r = c-1, c
            while (0 <= l < n and 0 <= r < n and
            s[l] == s[r]):
                count += 1
                l -= 1
                r += 1

        return count