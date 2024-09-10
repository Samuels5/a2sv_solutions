# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = Counter()
        winset = set()
        lossset = set()

        for val in matches:
            winset.add(val[0])
            lossset.add(val[1])
            loss[val[1]] += 1

        ans1 = []
        ans2 = []

        for val in winset:
            if val not in lossset:
                ans1.append(val)

        for val in lossset:
            if loss[val] == 1:
                ans2.append(val)

        return [sorted(ans1),sorted(ans2)] 