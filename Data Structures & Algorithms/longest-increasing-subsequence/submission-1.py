class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        maxlen = 0
        memo = {}

        def recursion(i, lst):
            nonlocal maxlen
            
            if tuple(lst) in memo:
                maxlen = max(maxlen, memo[tuple(lst)])
                memo[tuple(lst)] = maxlen

            if i == n:
                maxlen = max(maxlen, len(lst))
                memo[tuple(lst)] = maxlen
            else:
                new_lst = lst.copy()
                recursion(i+1, new_lst)
                while new_lst and new_lst[-1] >= nums[i]:
                    new_lst.pop()

                new_lst.append(nums[i])
                recursion(i+1, new_lst)
        
        recursion(0, [])
        return maxlen
        