# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curh = ListNode(0)
        curh.next = head
        cur = curh
        idx = 0

        while cur.next:
            idx +=1
            cur = cur.next
        cur = curh
        x = idx-n
        while x>0:
            cur = cur.next
            x-=1
        cur.next = cur.next.next
        
        return curh.next
