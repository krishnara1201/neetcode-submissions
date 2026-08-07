class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if s[0] != '0' else 0


        dp = [0] * n
        dp[n-1] = 1 if s[n-1] != '0' else 0

        for i in range(n-2,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            elif (s[i] == '1' or
                   (s[i] == '2' and s[i + 1] < '7')):
                dp[i] = dp[i+1] + 1
            else:
                dp[i] = dp[i+1]
        print(dp)
        return dp[0]


        