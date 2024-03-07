class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def back(val):
            if val == 1:
                return True
            elif val < 1:
                return False

            return back(val/3)
            
        return back(n)

        