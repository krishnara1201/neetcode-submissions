class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if n == 0:
            return []
        
        def dfs(i, cur):
            if i >= n:
                res.append(cur[::])
                return
            
            for j in range(len(digitToChar[digits[i]])):
                dfs(i+1, cur + digitToChar[digits[i]][j])
        
        dfs(0, "")
        return res