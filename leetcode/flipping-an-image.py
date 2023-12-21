class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        grid=[[] for i in range(len(image))]
        for raw in range(len(image)):
            for col in range(len(image[0])):
                if image[raw][col]==1:
                    grid[raw].append(0)
                else:
                    grid[raw].append(1)
        img=[]
        for val in grid:
            img.append(val[::-1])
        print(grid)
        return img


