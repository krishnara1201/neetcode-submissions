class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        l = 0

        max_price = 0

        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            else:
                max_price = max(max_price, prices[r] - prices[l])
            
        return max_price


