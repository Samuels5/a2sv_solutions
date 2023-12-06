class Solution:
    def totalMoney(self, n: int) -> int:
        count=0
        money=0
        weeks=ceil(n/7)
        for week in range(1,weeks+1):
            for day in range(7):
                if count==n:
                    break
                else:
                    money+=week+day
                    count+=1
        return money