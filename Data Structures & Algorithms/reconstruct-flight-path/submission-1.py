class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjset = collections.defaultdict(list)

        for from_i, to_i in tickets:
            heapq.heappush(adjset[from_i],to_i)
        
        # print(adjset)
        curr_path = ["JFK"]
        path = []

        while curr_path:
            
            node = curr_path[-1]
            if adjset[node]:
                curr_path.append(heapq.heappop(adjset[node]))
            else:
                path.append(curr_path.pop())
        
        path.reverse()
        return path

        

        