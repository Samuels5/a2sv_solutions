# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        pre = [0]
        for val in chalk:
            pre.append(val+pre[-1])

        k %= pre[-1]
        return bisect_right(pre,k)-1
