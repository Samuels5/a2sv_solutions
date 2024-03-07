# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        x = -1
        mid = 0
        if guess(n)==0:
            return n
        while left<=right:
            mid = (left+right)//2
            x = guess(mid)
            if x == 1:
                left = mid
            elif x == -1:
                right = mid
            elif x==0:
                return mid
        