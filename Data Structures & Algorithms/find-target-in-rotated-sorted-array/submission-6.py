class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        
        result = self.binary_search(nums, 0, pivot - 1, target)
        if result != -1:
            return result
        print(pivot)
        pivot = l
        return self.binary_search(nums, pivot, n - 1, target)

    def binary_search(self, nums, l, r, target):
        
        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
            