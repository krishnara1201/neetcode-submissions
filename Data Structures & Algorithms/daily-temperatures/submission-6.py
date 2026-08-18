class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n-1, -1, -1):
            
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            
            if stack:
                ind = stack[-1][0]
                res[i] = ind - i
            
            stack.append((i, temperatures[i])) 
        
        return res

                