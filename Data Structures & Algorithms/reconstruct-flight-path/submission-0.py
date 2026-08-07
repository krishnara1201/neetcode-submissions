class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjset = collections.defaultdict(list)

        for from_i, to_i in tickets:
            heapq.heappush(adjset[from_i],to_i)
        
        curr_path = ["JFK"]
        path = []

        while curr_path:
            
            node = curr_path[-1]
            if adjset[node]:
                curr_path.append(adjset[node].pop(0))
            else:
                path.append(curr_path.pop())
        
        path.reverse()
        return path

        

        