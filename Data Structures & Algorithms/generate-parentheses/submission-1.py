class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(ob, cb, cur):
            if len(cur) == 2*n:
                res.append(cur[::])
                return
            if ob == 0:
                dfs(1, cb, cur + "(")
                
            elif ob != n:
                dfs(ob + 1, cb, cur + "(")
                if (cb < ob):
                    dfs(ob, cb + 1, cur + ")")
            else:
                dfs(ob, cb + 1, cur + ")")                
        
        dfs(0,0,"")
        return res