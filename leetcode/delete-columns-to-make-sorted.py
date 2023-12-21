class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for col in range(len(strs[0])):
            c=[]
            for raw in range(len(strs)):
                c.append(strs[raw][col])
            if c!=sorted(c):
                count+=1
        return count



        