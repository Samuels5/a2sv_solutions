# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = []
        li = []
        def tra(root,stack):
            if not root: return None
            stack.append(root.val)
            tra(root.left,stack)
            tra(root.right,stack)
            li.append(stack.copy())
            stack.pop()
            
            
        tra(root,stack)
        maxi = []
        for val in li:
            maxi.append(abs(max(val)-min(val)))
        
        return max(maxi)
        