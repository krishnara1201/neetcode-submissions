class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        reqset = {}

        for a,b in prerequisites:
            if (((a in reqset) and (b in reqset[a])) or 
               ((b in reqset) and (a in reqset[b]))):
                return False
            if a not in reqset:
                reqset[a] = set()
            if b not in reqset:
                reqset[b] = set()
            reqset[a].add(b)
            reqset[b].add(a)

        return True
