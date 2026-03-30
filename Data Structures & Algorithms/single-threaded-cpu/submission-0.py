class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        triplet = []
        ind = 0
        for i,j in tasks:
            heapq.heappush(triplet,[i,j,ind])
            ind += 1
        
        time = 0
        res = []
        available = []
        while triplet or available:
            while triplet and triplet[0][0] <= time:
                eTime, pTime, ind = heapq.heappop(triplet)
                heapq.heappush(available, (pTime, ind))
            
            if not available:
                time = triplet[0][0]
                continue

            pTime, ind = heapq.heappop(available)
            time += pTime
            res.append(ind)

        return res
