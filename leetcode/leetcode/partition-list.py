# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1 = ListNode(0)
        first = d1
        d2 = ListNode(0)
        second = d2

        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
            head = head.next

        second.next = None
        first.next = d2.next

        return d1.next






        