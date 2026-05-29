class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if found and nums1[i] < nums2[j]:
                    result[i] = nums2[j]
                    break

                if nums1[i] == nums2[j]:
                    found = True

        return result
                