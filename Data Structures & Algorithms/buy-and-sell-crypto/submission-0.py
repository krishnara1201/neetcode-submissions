class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        l = 0
        r = 1
        max_profit = 0

        while l < r and r < n:
            cur_profit = prices[r] - prices[l]
            if cur_profit < 0:
                l = r
                r += 1
            else:
                max_profit = cur_profit if cur_profit > max_profit else max_profit
                r += 1
        
        return max_profit

