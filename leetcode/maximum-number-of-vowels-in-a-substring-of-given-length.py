class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vawel=0
        vawel+=s[:k].count('a')
        vawel+=s[:k].count('e')
        vawel+=s[:k].count('i')
        vawel+=s[:k].count('o')
        vawel+=s[:k].count('u')
        maxi=vawel
        i=0
        while i<len(s)-k:
            if s[i] in 'aeiou':
                vawel-=1
            if s[i+k] in 'aeiou':
                vawel+=1
            maxi=max(maxi,vawel)
            i+=1
        return maxi
        