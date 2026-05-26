class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for s in strs:
            if len(result) > len(s):
                result = result[:len(s)]
            for c in s:
                for i in range(len(result)):
                    if s[i] != result[i]:
                        result = result[:i]
                        break
        
        return result