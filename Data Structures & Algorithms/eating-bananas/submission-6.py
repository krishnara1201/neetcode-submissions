import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = l + (r-l)//2

            if self.canEat(m,piles,h):
                r = m
            else:
                l = m + 1
        return l


    def canEat(self, k, piles, h):
        count = 0
        for p in piles:
            count += math.ceil(p/k)
        return count <= h
