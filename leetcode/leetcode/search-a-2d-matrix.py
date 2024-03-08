class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        left = -1
        right = len(matrix)*len(matrix[0])
        while left+1<right:
            mid = (left + right)//2
            val = matrix[mid//col][mid%col]
            if val == target:
                return True
            elif val<target:
                left = mid
            else:
                right = mid
        return False