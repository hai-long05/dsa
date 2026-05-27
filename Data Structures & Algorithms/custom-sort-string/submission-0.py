class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        result = [] 
        for c in order:
            if c in count:
                result.extend(count[c] * [c])
                count[c] = 0
        

        for k in count:
            result.extend(count[k] * k)

        return ''.join(result)