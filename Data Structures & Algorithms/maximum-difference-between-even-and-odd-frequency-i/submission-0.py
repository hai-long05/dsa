class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        max_odd = 0
        min_even = len(s) + 1
        for k in freq:
            if freq[k] % 2:
                max_odd = max(max_odd, freq[k])
            else:
                min_even = min(min_even, freq[k])

        return max_odd - min_even