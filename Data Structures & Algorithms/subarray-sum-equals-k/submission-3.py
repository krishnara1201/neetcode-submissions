class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        n = len(nums)
        cursum = res = 0
        for i in range(n):
            cursum += nums[i]
            diff = cursum - k
            res += prefix.get(diff, 0)
            prefix[cursum] = prefix.get(cursum, 0) + 1
        return res
        