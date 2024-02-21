class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        for val in answers:
            if val == 0:
                count += 1
                continue
            if val not in d :
                count += val+1
                d[val] += val
            else:
                d[val] -= 1
                if d[val] == 0:
                    del d[val]
        return count