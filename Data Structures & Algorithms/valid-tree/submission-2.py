class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjset = {i:[] for i in range(n)}

        for a,b in edges:
            adjset[a].append(b)
            adjset[b].append(a)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            
            for nei in adjset[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
            