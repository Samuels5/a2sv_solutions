class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = defaultdict(int)
        for val in bills:
            if val == 5:
                d[val] += 1
            if val == 10:
                if 5 not in d:
                    return False
                d[5] -= 1
                if d[5] == 0:
                    del d[5]
                d[10] += 1
            if val == 20:
                if 10 in d and 5 in d:
                    d[10] -= 1
                    if d[10] == 0:
                        del d[10]
                    d[5] -= 1
                    if d[5] == 0:
                        del d[5]
                elif d[5]>2:
                    d[5] -= 3
                    if d[5] == 0:
                        del d[5]
                else:
                    return False

        return True
        