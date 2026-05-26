class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        apperance = {}
        for n in nums:
            apperance[n] = apperance.get(n, 0) + 1
            if apperance[n] > len(nums) / 2:
                return n

        return -1