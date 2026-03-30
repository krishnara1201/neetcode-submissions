class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            prereq[c].append(p)
        
        visited, cycle = set(), set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
        
            cycle.add(course)
           
            for c in prereq[course]:
                if not dfs(c):
                    return False
            visited.add(course)
            cycle.remove(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        else:
            return output