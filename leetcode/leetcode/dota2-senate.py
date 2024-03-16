class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()
        size = len(senate)
        for idx, val in enumerate(senate):
            if val == 'D':
                d.append(idx)
            else:
                r.append(idx)
        while d and r:
            if d[0]<r[0]:
                r.popleft()
                num = d.popleft()
                d.append(num+size)
            else:
                d.popleft()
                num = r.popleft()
                r.append(num+size)
        if r:
            return "Radiant"
        else:
            return "Dire"