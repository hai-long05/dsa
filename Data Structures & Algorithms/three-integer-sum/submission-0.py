class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])

                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return result