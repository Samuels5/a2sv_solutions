class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards))==len(cards):
            return -1
        d={}
        maxi=float('inf')
        for idx, val in enumerate(cards):
            if val in d:
                if maxi>idx-d[val]:
                    maxi=idx-d[val]
                d[val]=idx
            else:
                d[val]=idx
        return maxi+1


        