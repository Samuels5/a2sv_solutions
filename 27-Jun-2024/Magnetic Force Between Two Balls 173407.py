# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(num):
            count = 0
            i = 0
            while i < len(position):
                i = bisect_left(position, num + position[i])
                count += 1
                if count >= m:
                    return True
            return False

        left = -1
        right = 10**9
        while left + 1 < right:
            mid = (left + right)//2
            if helper(mid):
                left = mid
            else:
                right = mid

        return left