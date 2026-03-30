class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjset = {i:[] for i in range(n)}

        for a,b in edges:
            adjset[a].append(b)
            adjset[b].append(a)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return 
            visit.add(node)
            
            for nei in adjset[node]:
                if nei == prev:
                    continue
                dfs(nei, node)

        count = 0          
        for i in range(n):
            if i in visit:
                continue
            dfs(i, -1)
            count += 1

        return count