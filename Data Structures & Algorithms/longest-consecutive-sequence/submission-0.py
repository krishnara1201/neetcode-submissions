class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numset = set(nums)
        starts = []
        for num in numset:
            if num - 1 not in numset:
                starts.append(num)
        maxlen = 0
        for start in starts:
            curr = 1
            while start + 1 in numset:
                curr += 1 
                start += 1
            maxlen = max(maxlen, curr)
        return maxlen       