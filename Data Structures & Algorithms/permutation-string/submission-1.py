class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        p = len(s1) - 1
        while p <= len(s2):
            if sorted(s2[p - len(s1):p]) == sorted(s1):
                return True
            p += 1

        return False