class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mine=abs(target[0])+abs(target[1])
        goast=float('inf')
        for position in ghosts:
            goast1=abs(position[0]-target[0])+abs(position[1]-target[1])
            if goast1<goast:
                goast=goast1
        if goast<=mine:
            return False
        else:
            return True