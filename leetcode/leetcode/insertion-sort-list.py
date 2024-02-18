# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        cur = head

        while cur:
            li.append(cur.val)
            cur = cur.next

        li.sort()
        dumy = ListNode(0)
        d = dumy

        for val in li:
            new = ListNode(val)
            d.next = new
            d = d.next
        
        return dumy.next