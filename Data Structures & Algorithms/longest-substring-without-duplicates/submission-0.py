class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ""
        result = 0
        for c in s:
            while c in sub_string:
                sub_string = sub_string[1:]
            sub_string += c
            result = max(result, len(sub_string))

        return result