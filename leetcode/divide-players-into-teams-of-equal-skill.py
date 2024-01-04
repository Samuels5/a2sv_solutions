class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)//2
        skill1=skill[:n]
        skill2=skill[n:]
        skill2.reverse()
        ziped=list(zip(skill1,skill2))
        s=0
        for val in ziped:
            s+=val[0]*val[1]
        for val in range(len(ziped)-1):
            if sum(ziped[val])!=sum(ziped[val+1]):
                return -1
        return s
