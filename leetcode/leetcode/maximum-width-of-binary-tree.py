# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = []
        d = defaultdict(list)
        def back(root,level,val):
            if not root: return None
            d[level].append(val)
            back(root.left,level+1,val*2)
            back(root.right,level+1,val*2+1)
        back(root,0,0)
        num = -float('inf')
        for val in d.values():
            maxi = max(val)
            mini = min(val)
            re = maxi - mini + 1
            num = max(num,re)
        # print(d)
        return num