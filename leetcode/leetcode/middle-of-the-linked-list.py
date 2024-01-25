# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur.next:
            cur = cur.next
            size+=1
        cur1 = head
        for _ in range(size//2 +size%2):
            cur1 = cur1.next
        
        return cur1


        