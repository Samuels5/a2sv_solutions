class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=0
        j=len(piles)-2
        count=0
        while i<j:
            count+=piles[j]
            j-=2
            i+=1
        return count