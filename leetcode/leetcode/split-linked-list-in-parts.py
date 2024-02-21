# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        cur = head
        li = []
        num = n//k
        re = n%k
        for val in range(k):
            head = cur
            for t in range(num + (val<re)-1):
                if cur: cur = cur.next

            if cur:
                cur.next, cur = None, cur.next
            li.append(head)
        return li

        