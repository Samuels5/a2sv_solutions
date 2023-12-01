class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        i=num//3
        if num%3==0:
            return [int(i-1),int(i),int(i+1)]

        return []