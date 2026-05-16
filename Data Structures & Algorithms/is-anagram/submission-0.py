class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_s = dict()
        letter_t = dict()
        for i in range(len(s)):
            if s[i] in letter_s:
                letter_s[s[i]] = letter_s[s[i]] + 1
            else:
                letter_s[s[i]] = 1
            
            if t[i] in letter_t:
                letter_t[t[i]] = letter_t[t[i]] + 1
            else:
                letter_t[t[i]] = 1

        return letter_s == letter_t