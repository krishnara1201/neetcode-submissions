class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        n = len(position)

        for i in range(n):
            stack.append(i)
            curr_time = (target - position[i])/speed[i]
            for ind in stack[:-1]:
                ind_time = (target - position[ind])/speed[ind]
                print(curr_time <= ind_time)
                print(position[i] <= position[ind])
                if ((curr_time <= ind_time) and (position[i] <= position[ind])) or ((curr_time >= ind_time) and (position[i] >= position[ind])):
                    stack.pop()
                    break
            
        return len(stack)
            
            
