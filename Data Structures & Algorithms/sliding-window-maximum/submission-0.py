class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(k, len(nums) + 1):
            result.append(max(nums[i - k:i]))

        return result