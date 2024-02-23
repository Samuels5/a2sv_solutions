class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        while tickets[k]:
            if tickets[i]:
                count += 1
                tickets[i] -= 1
            i += 1
            if i == len(tickets):
                i = 0
        return count


        