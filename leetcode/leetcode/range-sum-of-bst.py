# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        def cal(root):
            if not root: return None
            stack.append(root.val)
            cal(root.left)
            cal(root.right)
        cal(root)

        re = 0
        for val in stack:
            if low <= val <= high:
                re += val

        return re
