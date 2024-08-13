# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for recipe, ing in zip(recipes, ingredients):
            for i in ing:
                indegree[recipe] += 1
                graph[i].append(recipe)
        
        answer = []
        queue = deque(supplies)
        recipes = set(recipes)
        
        while queue:
            x = queue.popleft()
            if x in recipes:
                answer.append(x)
                
            for i in graph[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return answer