class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def back(val):
            if val == 1:
                return True
            elif val < 1:
                return False

            return back(val/4)
            
        return back(n)