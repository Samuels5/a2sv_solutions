# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        if left == right:
            return head
        idx = 0
        cur = ListNode(0)
        cur.next = head
        first = cur
        second = None
        third = None
        while cur:
            if idx == left-1:
                temp = cur.next
                f1 = cur
                cur.next = None
                cur = temp
                second = temp
                # print(cur.val)
            if idx == right-1:
                third = cur.next
                
                cur.next = None
                cur = third
                # print(cur.val)
            if cur == None:
                break
            idx += 1
            cur = cur.next
        f = second
        s = f.next
        # print(first.val,second.val,third.val)
        while s:
            temp = s.next
            s.next = f
            f = s
            s = temp
        second.next = third
        second = f
        f1.next = second

        # print(first.val,second.val,third.val)

        
        return first.next

        

        