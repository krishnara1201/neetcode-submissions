class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_index, maxlen = 0, 0
        n = len(s)
        for c in range(n):
            l,r = c, c 
            while (0 <= l < n and 0 <= r < n and
                    s[l] == s[r]):
                if (r - l + 1) > maxlen:
                    res_index = l
                    maxlen = r - l + 1
                l -= 1
                r += 1

            l,r = c-1, c
            while (0 <= l < n and 0 <= r < n and
            s[l] == s[r]):
                if (r - l + 1) > maxlen:
                    res_index = l
                    maxlen = r - l + 1
                l -= 1
                r += 1

        return s[res_index:res_index + maxlen]