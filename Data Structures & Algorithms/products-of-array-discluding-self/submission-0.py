class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p_prod = [1] * n
        s_prod = [1] * n
        
        for i in range(1,n):
            p_prod[i] = p_prod[i-1] * nums[i-1]
            s_prod[n-1-i] = s_prod[n-i] * nums[n-i]
        
        res = [1] * n
        for i in range(n):
            res[i] = p_prod[i] * s_prod[i]

        return res