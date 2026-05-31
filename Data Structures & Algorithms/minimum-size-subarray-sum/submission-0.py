class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 0
        curr = 0
        l, r = 0, 0
        while r < len(nums):
            curr += nums[r]
            while curr >= target:
                if result == 0:
                    result = r - l + 1
                result = min(result, r - l + 1)
                curr -= nums[l]
                l += 1
            r += 1

        return result
                