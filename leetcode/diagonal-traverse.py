class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        for raw in range(len(mat)):
            for col in range(len(mat[0])):
                d[raw+col].append(mat[raw][col])
        flag=1
        re=[]
        for val in d.values():
            if flag==1:
                re+=val[::-1]
                flag=0
            else:
                re+=val
                flag=1
                
        return re

        