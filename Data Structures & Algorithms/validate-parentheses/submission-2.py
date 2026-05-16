class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for c in s:
            if c in brackets_map:
                stack.append(brackets_map[c])
            else:
                if len(stack) == 0:
                    return False

                if stack[len(stack) - 1] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0