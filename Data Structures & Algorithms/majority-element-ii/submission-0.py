class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > len(nums) / 3 and n not in result:
                result.append(n)
                
        return result