# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new = []

        for val in nums:
            st = str(val)
            s = ''
            for num in st:
                s += str(mapping[int(num)])

            new.append(int(s))

        main = [(new[i], i) for i in range(len(new))]
        main.sort(key = lambda x: x[0])

        ans = []
        for val in main:
            ans.append(nums[val[1]])

        return ans
