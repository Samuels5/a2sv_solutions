# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        def cal(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            if p.val == q.val:
                return cal(p.left,q.right) and cal(p.right,q.left)
            else:
                return False  
        return cal(p,q)


        