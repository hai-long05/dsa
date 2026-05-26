class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        usage = 1
        while n > 0:
            n = n - usage
            usage += 1
            if n >= 0:
                rows += 1

        return rows
        