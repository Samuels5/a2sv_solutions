class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum, count = 0, 0
        for i in range(len(costs)):
            sum = sum + costs[i]
            if sum > coins:
                return count
            else:
                count += 1
        return count