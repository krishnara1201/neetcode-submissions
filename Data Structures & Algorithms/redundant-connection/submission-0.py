class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjset = {}
        for a,b in edges:
            if a not in adjset:
                adjset[a] = []
            if b not in adjset:
                adjset[b] = []
            adjset[a].append(b)
            adjset[b].append(a)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                res = [prev, node]
                return False
            visit.add(node)
            
            for nei in adjset[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        res = []
                 
        for i in range(n):
            dfs(i, -1)

        return res