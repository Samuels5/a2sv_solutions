class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0

        for val in range(maxDoubles):
            if target == 1:
                break
            if target % 2 == 0:
                count += 1
            else:
                count += 2
            target //= 2
            
        count += target - 1

        return count