class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dic1 = {}

        for i in s1:
            dic1[i] = dic1.get(i, 0) + 1


        if len(s2) < len(s1):
            return False
        
        l, r = 0, len(s1) 

        dic2 = {}

        for i in range(r):
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        
        while r <= len(s2):
            # print(dic2, r, len(s2))
            if dic2 == dic1:
                return True
            
            if r < len(s2):
                dic2[s2[r]] = dic2.get(s2[r], 0) + 1

                if dic2[s2[l]] == 1:
                    dic2.pop(s2[l])
                else:
                    dic2[s2[l]] -= 1

                l += 1
                r += 1
            
            else:
                break
            
        
        return False

