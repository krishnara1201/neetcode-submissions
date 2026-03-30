class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        stack = [intervals[0]]
        
        for nums in intervals:
            if nums[0] > stack[-1][1]:
                stack.append(nums)
            else:
                temp = stack.pop()
                new = [min(temp[0], nums[0]), max(temp[1], nums[1])]
                stack.append(new)
        
        return stack