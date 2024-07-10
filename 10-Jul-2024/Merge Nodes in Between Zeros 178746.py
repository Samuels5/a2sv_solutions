# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        while curr:
            if curr.next.val != 0:
                curr.val += curr.next.val
                curr.next = curr.next.next
            else:
                curr.next = curr.next.next
                curr = curr.next

        return head.next