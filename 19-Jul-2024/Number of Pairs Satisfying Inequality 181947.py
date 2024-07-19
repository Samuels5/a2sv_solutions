# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def help(i, j):
            if i == j:
                return [arr[i]], 0

            mid = (i + j) // 2
            left, cntL = help(i, mid)
            right, cntR = help(mid + 1, j)

            l = len(left) - 1
            r = len(right) - 1
            cntT = 0

            while 0 <= l and 0 <= r:
                if left[l] - right[r] > diff:
                    l -= 1
                else:
                    cntT += l + 1
                    r -= 1

            l = r = 0
            ret = []
            
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    ret.append(left[l])
                    l += 1
                else:
                    ret.append(right[r])
                    r += 1

            while l < len(left):
                ret.append(left[l])
                l += 1

            while r < len(right):
                ret.append(right[r])
                r += 1

            return ret, cntT + cntL + cntR

        arr = [a - b for a, b in zip(nums1, nums2)]
        return help(0, len(arr) - 1)[1]