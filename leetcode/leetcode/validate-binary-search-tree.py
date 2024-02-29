# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        li = []
        def cal(root):
            if not root: return None
            cal(root.left)
            li.append(root.val)
            cal(root.right)
        cal(root)
        return li == sorted(list(set(li)))

