class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        l = 0

        max_price = 0

        for r in range(n):
            cur_price = prices[r] - prices[l]
            if cur_price < 0:
                l = r
            else:
                max_price = max(max_price, cur_price)
            
        return max_price


