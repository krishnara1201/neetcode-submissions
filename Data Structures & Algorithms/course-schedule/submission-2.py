class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        reqset = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            reqset[a].append(b)

        print(reqset)
        def dfs(course):
            if course in visit:
                return False
            if reqset[course] == []:
                return True
            visit.add(course)
            for c in reqset[course]:
                if not dfs(c):
                    return False
            visit.remove(course)
            return True

        visit = set()
        for i in reqset.keys():
            print(visit, i)
            if not dfs(i):
                return False
            print(visit)
        return True

