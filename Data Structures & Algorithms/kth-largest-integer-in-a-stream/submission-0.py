class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
           heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        
        heapq.heappushpop(self.minHeap, val)

        return self.minHeap[0]
        
