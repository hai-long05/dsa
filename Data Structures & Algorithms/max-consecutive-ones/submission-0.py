class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                maxx = max(maxx, count)
            else:
                count = 0

        return maxx 