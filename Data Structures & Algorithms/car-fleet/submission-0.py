class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(p, s) for p, s in zip(position, speed)]
        stack = []
        
        for p, s in reversed(sorted(car)):
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and time <= stack[-2]:
                stack.pop()

        return len(stack)