class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_idx = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_idx.add(i)
                if len(zero_idx) > 1:
                    return [0] * len(nums)   
        
        res = []
        for i in range(len(nums)):
            if i in zero_idx:
                res.append(product)
            else:
                if len(zero_idx) > 0:
                    res.append(0)
                else:
                    res.append(product // nums[i])
        
        return res