class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []
        for i, c in enumerate(s_list):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ""

        while stack:
            s_list[stack.pop()] = ""

        return "".join(s_list)