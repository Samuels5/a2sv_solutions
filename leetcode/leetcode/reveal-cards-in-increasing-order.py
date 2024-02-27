class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        de = deque()
        
        while deck:
            poped = deck.pop()
            if not de:
                de.append(poped)
                continue
            po = de.pop()
            de.appendleft(po)
            de.appendleft(poped)

        return de
