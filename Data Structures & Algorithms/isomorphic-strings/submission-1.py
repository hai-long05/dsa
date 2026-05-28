class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cs_map = {}
        ct_map = {}
        for i in range(len(s)):
            if s[i] in cs_map and cs_map[s[i]] != t[i] or t[i] in ct_map and ct_map[t[i]] != s[i]:
                return False
            cs_map[s[i]] = t[i]
            ct_map[t[i]] = s[i]
 
        return True