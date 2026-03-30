class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = defaultdict(list)

        dist_heap = []

        for xi,yi in points:
            distance = -(xi**2 + yi**2)
            
            if distance in dist:
                dist[distance].append([xi,yi])
            else:
                dist[distance] = [[xi,yi]]
            
            dist_heap.append(distance)
        
        print(dist)
        heapq.heapify(dist_heap)
        
        while len(dist_heap) > k:
            val = heapq.heappop(dist_heap)
            if len(dist[val]) > 1:
                dist[val].pop()
            else:
                dist.pop(val)
        
        print(dist_heap)
        res = []
        vals = dist.values()
        for val in vals:
            for item in val:
                res.append(item)

        return res