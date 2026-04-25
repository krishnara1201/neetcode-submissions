class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            m = l + (r-l)//2
            d = 1
            curr = 0
            for w in weights:
                if curr + w <= m:
                    curr += w
                else:
                    curr = w
                    d += 1
            print(d, m, l, r)
            if d <= days:
                r = m
            else:
                l = m + 1
        
        return l
