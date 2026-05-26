class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i = 0 # nums1_copy
        j = 0 # nums2
        idx = 0
        # m + n == len(nums) 
        while j < n and i < m:
            if nums1_copy[i] < nums2[j]:
                nums1[idx] = nums1_copy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1

        while i < m:
            nums1[idx] = nums1_copy[i]
            i += 1
            idx += 1

        while j < n:
            nums1[idx] = nums2[j]
            j += 1
            idx += 1
        
        