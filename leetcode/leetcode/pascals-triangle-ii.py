class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def cal(li):
            if rowIndex==0:
                return[1]
            if rowIndex==1:
                return[1,1]

            returned= self.getRow(rowIndex-1)
            li=deque()
            li.appendleft(1)

            for i in range(1,len(returned)):
                li.append(returned[i-1]+returned[i])

            li.append(1)
            
            return li

        return(cal(rowIndex))
