class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums: 
            freq[n] = freq.get(n, 0) + 1

        res = []
        for i in range(k):
            key = max(freq, key=freq.get)
            res.append(key)
            freq[key] = -9999

# mydict = {'george': 16, 'amber': 19}
# print(list(mydict.keys())[list(mydict.values()).index(16)])
        return res