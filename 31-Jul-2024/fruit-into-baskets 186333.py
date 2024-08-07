# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        i = 0 
        j = 0
        fruit_count = 0
        map1 = {}

        while j < len(fruits):
            if fruits[j] not in map1:
                map1[fruits[j]] = 1
            else:
                map1[fruits[j]] += 1
            
            if len(map1) > k :
                while len(map1) > k:
                    map1[fruits[i]] -= 1
                    if map1[fruits[i]] == 0:
                        del(map1[fruits[i]])
                    i += 1
            
            if len(map1) <= k:
                fruit_count = max(fruit_count,j - i + 1)
            
            j += 1
        
        return fruit_count