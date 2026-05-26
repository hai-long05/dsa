class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack or a > 0 or stack[-1] < 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0:
                    if abs(a) == abs(stack[-1]):
                        stack.pop()
                        break
                    elif abs(a) > abs(stack[-1]):
                        stack.pop()
                        if not stack or stack[-1] < 0:
                            stack.append(a)
                            break
                    else:
                        break

        return stack