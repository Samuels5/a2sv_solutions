# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        size = len(profit)
        main = [(difficulty[i], profit[i]) for i in range(size)]
        main.sort(key = lambda x: x[1], reverse = True)
        worker.sort(reverse = True)
        count = 0
        i, j = 0, 0
        while i < len(worker) and j < size :
            if worker[i] < main[j][0]:
                j += 1
            else:
                count += main[j][1]
                i += 1
                
        return count
