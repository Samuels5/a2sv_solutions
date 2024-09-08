# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(root):
            if not root: return
            for val in root.children:
                dfs(val)
            ans.append(root.val)
            
        dfs(root)

        return ans
        