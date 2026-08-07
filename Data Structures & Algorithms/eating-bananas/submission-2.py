import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        l, r = 0, max_piles

        while l <= r:
            
            m = l + (r-l)//2
            eating_time = self.eating_time(piles, m)
            eating_time_plus = self.eating_time(piles, m + 1)
            print(l, r, m, eating_time, eating_time_plus)
            if (eating_time_plus < h and eating_time > h) or (eating_time == h):
                break
                
            if eating_time < h:
                l = m + 1
            else:
                r = m - 1

        return m
    
    def eating_time(self, piles, speed):
        count = 0
        if speed == 0:
            return float("inf")

        for pile in piles:
            count +=  math.ceil(pile/speed)
        return count