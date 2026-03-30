class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n, m = len(s), len(t)

        if n < m:
            return ""

        dic_t = {}

        for i in t:
            dic_t[i] = dic_t.get(i, 0) + 1
        
        need = len(dic_t)

        l = 0
        have = 0
        dic_win = {}
        min_win = [0,0]
        min_len = n + 1

        for r in range(n):
            print(l, r)
            if s[r] in dic_t:
                dic_win[s[r]] = dic_win.get(s[r], 0) + 1
                if dic_win[s[r]] == dic_t[s[r]]:
                    have += 1
            
            if need == have:
                if r - l + 1 < min_len:
                    min_len =  r - l + 1
                    min_win = [l, r]
            
            while need == have:

                while s[l] not in dic_t:
                    l += 1
                    if r - l + 1 < min_len:
                        min_len =  r - l + 1
                        min_win = [l, r]
                    
                
                if dic_win[s[l]] == dic_t[s[l]]:
                    have -= 1
                    dic_win[s[l]] -= 1
                    l += 1
                else:
                    dic_win[s[l]] -= 1
                    l += 1
                    min_len =  r - l + 1
                    min_win = [l, r]
            
        return s[min_win[0]: min_win[1] + 1] if min_len != (n + 1) else ""
                
            


