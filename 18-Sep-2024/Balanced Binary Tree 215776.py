# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = 0
        
        def dfs(root):
            nonlocal flag
            if flag: return 0
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if abs(l-r)>1:
                flag = 1
                return 0
            else:
                return max(r,l)+1

        dfs(root)

        return not flag