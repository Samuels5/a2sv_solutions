class Solution:
    def isHappy(self, n: int) -> bool:
        count=0
        while n<=2**31-1:
            n2=list(map(int,list(str(n))))
            n=0
            for i in n2:
                n+=i**2
            if n==1:
                return True
            count+=1
            if count>70:
                return False
        return False