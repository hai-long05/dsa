class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = 0
        while l <= r:
            m = (l + r) // 2
            
            if m ** 2 == x:
                return m

            if m ** 2 < x:
                result = m
                l = m + 1
            else:
                r = m - 1

        return result