class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate = max(piles)
        result = max_rate

        while min_rate <= max_rate:
            rate = (min_rate + max_rate) // 2
            sum_hours = 0
            for p in piles:
                sum_hours += math.ceil(p / rate)

            if sum_hours <= h:
                result = rate
                max_rate = rate - 1
            else:
                min_rate = rate + 1

        return result
