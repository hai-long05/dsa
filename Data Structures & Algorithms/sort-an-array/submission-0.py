class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            left = self.sortArray(nums[:len(nums)//2])
            right = self.sortArray(nums[len(nums)//2:])

            return self.merge(left, right)

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        while nums1 and nums2:
            if nums1[0] > nums2[0]:
                result.append(nums2.pop(0))
            else:
                result.append(nums1.pop(0))

        while nums1:
            result.append(nums1.pop(0))
        while nums2:
            result.append(nums2.pop(0))

        return result