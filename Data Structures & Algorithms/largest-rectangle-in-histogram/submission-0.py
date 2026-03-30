class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rstack = []
        lstack = []
        n = len(heights)

        left_heights = [0] * n
        right_heights = [n-1] * n
        
        
        for i in range(n):   
            while rstack and heights[i] < rstack[-1][0]:
                h, ind = rstack.pop()
                right_heights[ind] = i - 1
            rstack.append([heights[i], i])

        for i in range(n-1, -1 ,-1):
            
            while lstack and heights[i] < lstack[-1][0]:
                h, ind = lstack.pop()
                left_heights[ind] = i + 1
            
            lstack.append([heights[i], i])
        
        print(left_heights, right_heights)
        max_area = 0
        for i in range(n):
            area = (right_heights[i] - left_heights[i] + 1) * heights[i]
            max_area = max(max_area, area)
        
        return max_area

            
            
        