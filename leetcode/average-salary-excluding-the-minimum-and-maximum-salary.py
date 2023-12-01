class Solution:
    def average(self, salary: List[int]) -> float:
        maxi=max(salary)
        mini=min(salary)
        salary.remove(maxi)
        salary.remove(mini)
        ava=sum(salary)/len(salary)
        return ava