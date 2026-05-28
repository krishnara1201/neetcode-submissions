class StockSpanner:

    def __init__(self):
        self.stack = []
        self.ind = 0

    def next(self, price: int) -> int:
        
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()

        if self.stack:
            span = self.ind - self.stack[-1][0]
        else:
            span = self.ind + 1
        
        self.stack.append((self.ind, price))
        self.ind += 1
    
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)