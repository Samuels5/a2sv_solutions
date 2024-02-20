class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1]-x[0])
      
        total = 0
        for i, x in enumerate(tasks):
            total += x[0]
            
            if total<x[1]:
                total = x[1]
        
        return total