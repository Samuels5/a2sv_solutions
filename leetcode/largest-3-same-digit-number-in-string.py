class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a=[]
        for value in list(num):
            if ''.join([value]*3) in num:
                a.append(''.join([value]*3))
        if a == []:
            return ''
        return max(a)