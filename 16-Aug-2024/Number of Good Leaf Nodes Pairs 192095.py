# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1

            merged = [i+1 for i in left+right if i+1 < distance]
            return merged
        
        dfs(root)

        return self.result