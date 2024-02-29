# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def tra(root):
            if not root: return None

            tra(root.left)
            stack.append(root.val)
            tra(root.right)
        tra(root)
        return stack[k-1]


        