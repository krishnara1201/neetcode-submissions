class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l,r = 0, n - 1
        k = 0
        while 0<=r<n and nums[r] == val:
            r -= 1
            k += 1
        
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                while nums[r] == val:
                    r -= 1
                    k += 1
            l += 1
        return n - k