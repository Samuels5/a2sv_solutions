# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {val:idx+1 for idx,val in enumerate(alpha)}
        arr = []

        for  val in s:
            arr.append(str(d[val]))
            
        num = int(''.join(arr))

        for i in range(k):
            num = sum(list(map(int,list(str(num)))))

        return num

