class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        for c in s:
            if c == t[0]:
                t = t[1:]
                if t == "":
                    return 0

        return len(t)