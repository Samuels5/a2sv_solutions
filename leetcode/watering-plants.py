class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i=0
        count=0
        capacity_max=capacity
        while i<len(plants):
            if capacity-plants[i]>=0:
                capacity-=plants[i]
                i+=1
                count+=1
                print(count)
            else:
                count+=2*i
                capacity=capacity_max
        return count