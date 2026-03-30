class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i-1])
            right_max[n-i-1] = max(right_max[n-i], height[n-i])

        res = 0

        for i in range(n):
            res += max(min(left_max[i], right_max[i]) - height[i], 0)
        
        return res