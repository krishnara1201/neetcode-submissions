class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        res = sum(matchsticks)
        m = math.sqrt(res)

        if int(m) != m:
            return False
        visit = set()
        def dfs(i, curr):
            if i == n and curr != m:
                return False
            elif curr == m:
                return True
            elif i in visit:
                return dfs(i + 1, curr)
            else:
                visit.add(i)
                bool1 = dfs(i+1, curr + matchsticks[i]) 
                visit.remove(i)
                bool2 = dfs(i + 1, curr)
                return bool1 or bool2
        
        return dfs(0, 0)


