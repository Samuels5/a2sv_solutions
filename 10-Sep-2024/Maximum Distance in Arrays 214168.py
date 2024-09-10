# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        main = []
        
        for idx, val in enumerate(arrays):
            for num in val:
                main.append((idx,num))

        main.sort(key = lambda x: x[1])

        i = 0
        maxi = -float('inf')
        while main[i][0] == main[-1][0]:
            i += 1
        maxi = max(maxi,main[-1][1]-main[i][1])

        j = len(main)-1
        while main[j][0] == main[0][0]:
            j -= 1

        maxi = max(maxi,main[j][1]-main[0][1])

        return maxi