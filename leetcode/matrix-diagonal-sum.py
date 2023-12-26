class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        c=[]
        d=[]

        for raw in range(len(mat)):
            for col in range(len(mat[0])):
                if raw-col==0:
                    d.append(mat[raw][col])
                if raw + col == len(mat) -1:
                    c.append(mat[raw][col])
        re=sum(d)+sum(c)
        if len(d)%2 != 0:
            re-=d[len(d)//2]
        return re