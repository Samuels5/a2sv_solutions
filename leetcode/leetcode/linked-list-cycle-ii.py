# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        idx = 0
        d = set([])
        while idx < 10000 and cur:
            if cur in d:
                return cur
            else:
                d.add(cur)
            idx += 1
            cur = cur.next

        return None

        