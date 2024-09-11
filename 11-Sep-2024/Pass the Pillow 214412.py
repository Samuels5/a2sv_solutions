# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num = 1
        flag = 1
        for i in range(time):
            if num == n:
                flag = 0
            if num == 1:
                flag = 1
            if flag:
                num += 1
            else:
                num -= 1
                
        return num
