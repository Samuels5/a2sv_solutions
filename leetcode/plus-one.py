class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for digit in digits:
            s+=str(digit)
        num=int(s)+1
        return list(map(int,str(num)))  
        