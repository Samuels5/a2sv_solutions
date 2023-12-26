class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height=heights.copy()
        n=len(heights)
        for num1 in range(n-1):
            for num2 in range(n-1):
                if heights[num2]<heights[num2+1]:
                    heights[num2],heights[num2+1]=heights[num2+1],heights[num2]
        arr=[]
        for val in heights:
            idx=height.index(val)
            arr.append(names[idx])
        return arr
        