# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        
        i = 0
        arr = []
        
        for row in range(m):
            new = []
            for col in range(n):
                new.append(original[i])
                i += 1
            arr.append(new)
            
        return arr