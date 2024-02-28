# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def transvers(root):
            if root:
                li.append(root.val)
                transvers(root.left)
                transvers(root.right)
        transvers(root)
        count = Counter(li)
        maxi = max(count.values())
        re = []
        for key,val in count.items():
            if val == maxi:
                re.append(key)
        return re

        