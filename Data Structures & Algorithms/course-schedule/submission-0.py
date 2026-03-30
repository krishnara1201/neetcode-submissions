class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjlist = {i:[] for i in range(numCourses)}

        for c1, c2 in prerequisites:
            adjlist[c1].append(c2)

        visit = set()
        
        def dfs(course):
            if course in visit:
                return False
            if adjlist[course] == []:
                return True
            
            visit.add(course)
            for prereq in adjlist[course]:
                if not dfs(prereq):
                    return False
            adjlist[course] = []
            visit.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True