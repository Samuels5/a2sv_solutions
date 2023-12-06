class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        re=[]
        for amount in candies:
            if amount + extraCandies >= maxi:
                re.append(True)
            else:
                re.append(False)
        return re
