class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 1
        for bed in flowerbed:
            if bed == 0:
                count += 1
            else:
                count = 0

            if count == 3:
                n -= 1
                count = 1

        n -= 1 if count == 2 else 0
        return n <= 0