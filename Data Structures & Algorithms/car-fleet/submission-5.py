class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        n = len(position)

        for i in range(n):
            stack.append(i)
            curr_time = (target - position[i])/speed[i]
            for ind in range(len(stack) - 1):
                ind_time = (target - position[stack[ind]])/speed[stack[ind]]
                print(curr_time <= ind_time)
                print(position[i] <= position[stack[ind]])
                if ((curr_time <= ind_time) and (position[i] <= position[stack[ind]])) or ((curr_time >= ind_time) and (position[i] >= position[stack[ind]])):
                    if position[i] < position[stack[ind]]:
                        stack.pop()
                    else:
                        stack.pop(stack[ind])
                    break
            
        return len(stack)
            
            
