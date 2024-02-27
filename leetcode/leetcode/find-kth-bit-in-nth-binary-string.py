class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def calc(n):
            if n == 0:
                return "0"
            s = ""
            returned = calc(n-1)

            for ind in returned:
                if ind == "0":
                    s += "1"
                else:
                    s += "0"
            
            return returned + "1" + s[::-1]

        val = calc(n)
        
        return val[k-1]