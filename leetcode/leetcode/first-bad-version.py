# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
            if not isBadVersion(left) and isBadVersion(right) and left +1 == right:
                return right


        