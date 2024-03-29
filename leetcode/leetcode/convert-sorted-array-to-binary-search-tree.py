# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def back(left, right):
            if left > right: return None
            mid = (left + right)//2
            left = back(left,mid-1)
            right = back(mid+1,right)
            return TreeNode(nums[mid],left,right)
            
        return back(0,len(nums)-1)



        