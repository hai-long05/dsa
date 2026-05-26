class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pair = {}

        for i in range(len(nums)):
            if nums[i] in pair and i - pair[nums[i]] <= k:
                return True
            pair[nums[i]] = i

        return False