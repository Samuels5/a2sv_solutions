class Solution:
    def mySqrt(self, x: int) -> int: 
        left = 0
        right = x
        if x == 1:
            return 1
        while left < right:
            mid = (left + right)//2
            if mid**2 < x:
                left = mid
            elif mid**2 >x:
                right = mid
            else:
                left = mid
                break
            if left+1 == right:
                return left
        return left

        