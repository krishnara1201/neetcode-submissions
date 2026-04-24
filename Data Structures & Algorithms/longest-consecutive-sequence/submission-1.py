class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numset = set(nums)
        maxlen = 0
        for num in numset:
            if num - 1 not in numset:
                leng = 1
                while num + leng in numset:
                    leng += 1
                maxlen = max(maxlen, leng)
        return maxlen       