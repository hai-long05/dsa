class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows - 1
        mid = 0
        while l <= r and rows > 1:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, cols - 1
        while l <= r: 
            c_mid = (l + r) // 2
            if matrix[mid][c_mid] == target:
                return True
             
            if matrix[mid][c_mid] > target:
                r = c_mid - 1
            else:
                l = c_mid + 1

        return False