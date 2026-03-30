class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0, len(arr) - 1
        res = []

        while l <= r and r - l + 1 > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        
        for i in range(l, r + 1):
            res.append(arr[i])

        return res