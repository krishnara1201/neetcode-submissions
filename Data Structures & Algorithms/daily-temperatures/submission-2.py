class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        res = [0] * n
        stack = []

        # for i in range(n - 1, -1, -1):
        #     if not stack:
        #         stack.append([temperatures[i], i])
            
        #     if temperatures[i] > 

        for i in range(n):
            
            while stack and temperatures[i] > stack[-1][0]:
                temp = stack.pop()
                res[temp[1]] = i - temp[1]

            stack.append([temperatures[i], i])

        return res
            