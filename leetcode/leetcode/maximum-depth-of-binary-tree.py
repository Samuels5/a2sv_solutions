# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def cal(root):
            if not root: return 0
            left = 1 + cal(root.left)
            right = 1 + cal(root.right)
            return max(left,right)
        return cal(root)


        # maxi = []
        # num = 0
        # def tra(root):
        #     num +=1
        #     print(num)
        #     if root:
        #         num +=1
        #         tra(root.left)
        #         tra(root.right)
        #         print(num)

        # tra(root)
        # return maxi

        