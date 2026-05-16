class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for n in nums:
            current = n
            streak = 0
            while current in nums_set:
                current += 1
                streak += 1
            res = max(res, streak)

        return res