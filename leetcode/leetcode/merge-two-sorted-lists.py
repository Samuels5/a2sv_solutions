# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1)
        head = ListNode(None)
        head1 = head
        first = list1
        second = list2

        if first and not second:
            return first
        if second and not first:
            return second
        if not first and not second:
            return first

        if first.val < second.val:
            head1.val = first.val
            first = first.next 
        else:
            head1.val = second.val
            second = second.next

        while first and second:
            if first.val < second.val:
                head1.next = first
                head1 = head1.next
                first = first.next
            else:
                head1.next = second
                head1 = head1.next
                second = second.next

        if first:
            head1.next = first
        else:
            head1.next = second
        
        return head

