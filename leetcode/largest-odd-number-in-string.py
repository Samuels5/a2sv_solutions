class Solution:
    def largestOddNumber(self, num: str) -> str:
        nums=list(num)
        while True:
            if len(nums)==0:
                return ''
            if int(nums[-1])%2!=0:
                return ''.join(nums)
            else:
                nums.pop()
        