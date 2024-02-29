# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        li = []
        def tra(root,stack):
            if not root: return None
            stack.append(root.val)
            tra(root.left,stack)
            tra(root.right,stack)
            if not root.left and not root.right:
                li.append(stack.copy())
            stack.pop()
        tra(root,stack)

        re = 0
        for val in li:
            s = ''
            for num in val:
                s+=str(num)
            re += int(s)

        return re
