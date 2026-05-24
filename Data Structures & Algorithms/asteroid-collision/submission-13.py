class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
            elif not(stack[-1] > 0 and a < 0):
                stack.append(a)
            else:
                breakval = False
                while stack and stack[-1] > 0 and a < 0:
                    b = stack.pop()
                    if abs(b) != abs(a):
                        if abs(a) < abs(b):
                            a = b
                    else:
                        breakval = True
                        break
                if not breakval:
                    stack.append(a)
        return stack