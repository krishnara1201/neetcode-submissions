class StockSpanner:

    def __init__(self):
        self.stack = []
        self.ind = 0

    def next(self, price: int) -> int:
        
        while self.stack and self.stack[-1][1] < price:
            ind,val = self.stack.pop()
        
        if self.stack:
            j = self.stack[-1][0]
        else:
            j = 0
        
        self.stack.append((self.ind, price))
        self.ind += 1
        res = self.ind - j - 1
        return res if res else 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)