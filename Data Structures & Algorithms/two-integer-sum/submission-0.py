class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            curr_diff = target - nums[i]
            if curr_diff in diff:
                return [diff[curr_diff], i]
            else:
                diff[nums[i]] = i
        