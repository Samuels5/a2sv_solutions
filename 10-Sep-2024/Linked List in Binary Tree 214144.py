# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        collect = []
        stack = []
        def cal(root):
            if not root: return 
            stack.append(root.val)
            if not root.left and not root.right:
                collect.append(stack.copy())
            cal(root.left)
            cal(root.right)
            stack.pop()
        h = []
        def nex(head):
            if not head: return 
            h.append(head.val)
            nex(head.next)
        nex(head)

        cal(root)
        # print(h,collect)
        
        for val in collect:
            for i in range(len(val)):
                j = 0
                for v in val[i:]:
                    if v == h[j]:
                        j += 1
                    else:
                        break
                    if j == len(h):
                        return True

        return False