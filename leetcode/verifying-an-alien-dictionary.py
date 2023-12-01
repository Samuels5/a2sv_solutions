class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alp = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i in range(26):
            d[order[i]] = alp[i]

        def f(st):
            normal = ''
            for i in st:
                normal += d[i]
            return normal

        for i in range(len(words)-1):
            if f(words[i]) > f(words[i+1]):
                return False

        return True
