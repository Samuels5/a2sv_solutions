class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        prev, B_prev = 1, 2
        current = 0

        for loop in range(1,n-1):
            current = prev + B_prev 
            prev = B_prev
            B_prev = current

        return current