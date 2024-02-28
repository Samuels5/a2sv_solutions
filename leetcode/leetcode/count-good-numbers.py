class Solution:
    def __init__(self):
        self.M = 1000_000_007

    def countGoodNumbers(self, n: int) -> int:
        def myPow(x, m):
            if m==0:
                return 1
    
            half=myPow(x,m//2)
            if m%2==0:
                return (half*half)%(self.M)
            return (half*half*x)%self.M

        even=(n+1)//2
        odd=n//2
        
        return (myPow(5,even)*myPow(4,odd))%self.M