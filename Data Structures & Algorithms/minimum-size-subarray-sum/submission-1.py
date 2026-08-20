class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = l = 0
        n = len(nums)
        min_len = n + 1
        for r in range(n):
            while cur_sum + nums[r] >= target:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            cur_sum += nums[r]
        return min_len if min_len < n + 1 else 0