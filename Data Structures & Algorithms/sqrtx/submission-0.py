class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 0, x

        while True:
            m = l + (r-l)//2

            if m * m == x or (m*m < x and (m+1)*(m+1) > x):
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1