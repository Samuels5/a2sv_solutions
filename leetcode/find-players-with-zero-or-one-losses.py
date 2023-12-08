class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = dict()
        for m in matches:
            if m[0] not in d:
                d[m[0]] = 0
            if m[1] not in d:
                d[m[1]] = 0
            if m[1] in d:
                d[m[1]] += 1
        zero_losses = []
        one_losses = []
        for key in d.keys():
            if d[key] == 0:
                zero_losses.append(key)
            elif d[key] == 1:
                one_losses.append(key)
        return [sorted(zero_losses),sorted(one_losses)]