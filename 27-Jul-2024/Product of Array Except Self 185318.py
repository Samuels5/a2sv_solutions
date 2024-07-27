# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sumi = 1
        for val in nums:
            sumi *= val
            
        if 0 in nums and nums.count(0)>1:
            return [0]*len(nums)
            
        if 0 in nums:
            arr = []
            sumi = 1
            for val in nums:
                if val != 0:
                    sumi *= val
            for val in nums:
                if val != 0:
                    arr.append(0)
                else:
                    arr.append(sumi)

            return arr

        li = []
        if 0 not in nums:
            for val in nums:
                li.append(sumi//val)

        return li
        