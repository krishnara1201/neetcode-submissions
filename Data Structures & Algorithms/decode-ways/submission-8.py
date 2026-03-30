class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        nums = set([str(i) for i in range(1,27)])
        if s[0] not in nums:
            return 0
        
        if n == 1:
            return 1
        
        dp = [0] * n
        dp[0] = 1 
        if ((s[0:2] in nums) and (s[1] in nums)):
            dp[1] = 2
        elif ((s[0:2] in nums) or (s[1] in nums)):
            dp[1] = 1
        else:
            return 0
        
        for i in range(2,n):
            if s[i] in nums:
                dp[i] = dp[i-1]
            if s[i-1:i+1] in nums:
                dp[i] += dp[i-2]
            if (s[i] not in nums) and (s[i-1:i+1] not in nums):
                return 0
        
        return dp[n-1]
            
