class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = n - k % n
        nums[:] = nums[r:n] + nums[:r]