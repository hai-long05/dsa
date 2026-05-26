class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        result = 0

        def can_ship(cap):
            ships, curr = 1, cap
            for w in weights:
                if curr - w < 0:
                    ships += 1
                    curr = cap
                curr = curr - w

            return ships <= days

        while l <= r:
            m = (l + r) // 2
            if can_ship(m):
                result = m
                r = m - 1
            else:
                l = m + 1
        
        return result