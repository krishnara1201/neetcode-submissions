class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = collections.Counter(list(s))
        freq = []

        for key in count.keys():
            heapq.heappush(freq, (-count[key], key))

        res = ""
        while freq:
            i, c = heapq.heappop(freq)
            
            if res and c == res[-1]:
                return ""
            res += c
            i += 1
            if i != 0:
                heapq.heappush(freq, (i, c))
        
        return res
