class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d={}
        re=[]
        for i in range(len(s)):
            re.append(s[indices.index(i)])
        return ''.join(re)
