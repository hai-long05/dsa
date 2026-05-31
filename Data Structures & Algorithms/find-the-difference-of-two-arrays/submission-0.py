class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        list1 = []
        
        set2 = set(nums2)
        list2 = []
        

        for n in nums1:
            if n not in set2 and n not in list1:
                list1.append(n)

        for n in nums2:
            if n not in set1 and n not in list2:
                list2.append(n)

        return [list1, list2]