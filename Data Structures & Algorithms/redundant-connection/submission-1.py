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
        cycle = set()
        cyclestart = -1

        def dfs(node, prev):
            nonlocal cyclestart
            if node in visit:
                cyclestart = node
                return True
            
            visit.add(node)
            for nei in adjset[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    if cyclestart != -1:
                        cycle.add(node)
                    if node == cyclestart:
                        cyclestart = -1 
                    return True
            return False

        dfs(1, -1)

        for a,b in reversed(edges):
            if a in cycle and b in cycle:
                return [a,b]
        
        return []

        return res