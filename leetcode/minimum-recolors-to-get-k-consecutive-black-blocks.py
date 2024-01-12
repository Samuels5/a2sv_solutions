class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum_change=k   
        for i in range(0,len(blocks)):
            b=blocks[i:i+k].count("B") 
            if(b>=k):     
                return 0
            minimum_change=min(minimum_change,k-b)
        return minimum_change
        