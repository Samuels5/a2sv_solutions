# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        d = defaultdict(int)
        def dfs(root):
            if not root: return
            if root.left:
                d[(root.val,'L')] = root.left.val
                d[(root.left.val,'U')] = root.val
            if root.right:
                d[(root.val,'R')] = root.right.val
                d[(root.right.val,'U')] = root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        # print(d)
        # q = deque(startValue)
        # while q:

        
        ans = ''
        s = set()
        flag = 0
        def find(val, st):
            s.add(val)
            if val == destValue: 
                return st
            if (val,'U') in d and d[(val,'U')] not in s:
                x = find(d[(val,'U')] ,'U')
                if x:
                    return x+st
            if (val,'L') in d and d[(val,'L')] not in s:
                x = find(d[(val,'L')] ,'L')
                if x:
                    return x+st
            if (val,'R') in d and d[(val,'R')] not in s:
                x = find(d[(val,'R')] ,'R')
                if x:
                    return x+st

        return find(startValue, '')[::-1]
