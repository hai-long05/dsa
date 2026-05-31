class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                if j - i >= 1 and curr % k == 0:
                    return True

        return False