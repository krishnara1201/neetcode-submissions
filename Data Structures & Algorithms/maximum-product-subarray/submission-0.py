class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod = 1, 1
        n = len(nums)
        res = nums[0]

        for num in nums:
            max_prod = max(max_prod * num, num, min_prod * num)
            min_prod = min(max_prod * num, num, min_prod * num)
            res = max(res, max_prod)

        return res
            