class MedianFinder:

    def __init__(self):
        self.right_half = []
        self.left_half = []

    def addNum(self, num: int) -> None:
        if self.right_half and num > self.right_half[0]:
            heapq.heappush(self.right_half, num)
        else:
            heapq.heappush(self.left_half, -num)

        if len(self.left_half) > len(self.right_half) + 1:
            val = -1 * heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, val)
        if len(self.right_half) > len(self.left_half) + 1:
            val = -1 * heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, val)
        

    def findMedian(self) -> float:
        if len(self.left_half) > len(self.right_half):
            return -1 * self.left_half[0]
        if len(self.right_half) > len(self.left_half):
            return self.right_half[0]
        else:
            return (-1 * self.left_half[0] + self.right_half[0]) / 2.0
        
        