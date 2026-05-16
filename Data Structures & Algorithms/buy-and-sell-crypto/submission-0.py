class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_idx = 0
        p = 1
        while p < len(prices):
            max_profit = max(max_profit, prices[p] - prices[min_idx])

            if prices[p] < prices[min_idx]:
                min_idx = p
            
            p += 1

        return max_profit