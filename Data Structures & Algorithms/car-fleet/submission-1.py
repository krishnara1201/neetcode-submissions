class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        n = len(position)

        for i in range(n):
            stack.append(i)
            for ind in stack[:-1]:
                print(stack)
                if ((target - position[i])/speed[i] <= (target - position[ind])/speed[ind]):
                    stack.pop(ind)
                    break
            
        return len(stack)
            
            
