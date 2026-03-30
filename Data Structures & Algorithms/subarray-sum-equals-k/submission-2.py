class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        curSum = res = 0

        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSum.get(diff, 0)

            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1

        return res