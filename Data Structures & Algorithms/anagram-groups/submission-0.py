class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            letter_count = [0] * 26
            for c in s:
                letter_count[ord(c) - ord('a')] += 1
            result[tuple(letter_count)].append(s)

        return list(result.values())
            