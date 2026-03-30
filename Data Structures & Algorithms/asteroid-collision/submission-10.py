class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if not stack or not(stack[-1] > 0 and i < 0):
                stack.append(i)
            else:
                val = i
                both = False
                while stack and (stack[-1] > 0 and val <= 0):
                    top = stack.pop()
                    diff = val + top
                    if diff != 0:
                        if abs(val) < abs(top):
                            val = top
                    else:
                        both = True
                        break
                if not both:
                    stack.append(val)
        return stack