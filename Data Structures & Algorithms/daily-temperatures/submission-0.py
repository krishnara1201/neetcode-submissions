class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        for i in range(n):
            stack.append([temperatures[i], i])
            
