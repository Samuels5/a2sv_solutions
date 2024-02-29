# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def tra(root,level):
            if not root: return None
            d[level].append(root.val)
            tra(root.left,level+1)
            tra(root.right,level+1)
        
        tra(root,0)
        print(d)
        flag = 0
        li = []
        for key,val in sorted(d.items()):
            if not flag:
                flag = 1
                li.append(val)
            elif flag:
                flag = 0
                li.append(val[::-1])
        return li

        