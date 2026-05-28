class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_map = {}
        s_map = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        
        for i in range(min(len(pattern), len(s))):
            if (s[i] in s_map and s_map[s[i]] != pattern[i]) or (pattern[i] in p_map and p_map[pattern[i]] != s[i]):
                return False
            p_map[pattern[i]] = s[i]
            s_map[s[i]] = pattern[i]

        return True