import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        l, r = 0, max_piles

        while l <= r:
            m = l + (r-l)//2

            if self.eating_time(piles, m) > h:
                l = m + 1
            if self.eating_time(piles, m) < h and self.eating_time(piles, m - 1) > h:
                break
            else:
                r = m - 1

        return m
    
    def eating_time(self, piles, speed):
        count = 0
        for pile in piles:
            count += pile + math.ceil(pile/speed)
        return count