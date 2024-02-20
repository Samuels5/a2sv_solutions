class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x: abs(x[0]-x[1]), reverse = True)
        total = 0
        a = b = len(costs)/2
        for a1,b1 in costs:
            if b == 0 or (a and a1<=b1):
                total += a1
                a -= 1
            else:
                total += b1
                b -= 1
        return total


