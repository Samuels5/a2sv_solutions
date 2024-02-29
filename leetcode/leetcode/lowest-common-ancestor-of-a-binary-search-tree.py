# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        li1 = []
        li2 = []
        def cal(root,stack):
            if not root: return None
            stack.append(root.val)

            if root.val ==p.val:
                li1.extend(stack)
            if root.val == q.val:
                li2.extend(stack)

            cal(root.left,stack)
            cal(root.right,stack)
            stack.pop()
            
        cal(root,stack)
        num = 0
        idx = 0
        while idx<len(li1) and idx < len(li2):
            if li1[idx] != li2[idx]:
                break
            num = li1[idx]
            idx += 1

        global r
        r = 0

        def find(root):
            if not root: return None
            global r
            if root.val == num:
                r = root

            find(root.left)
            find(root.right)

        find(root)

        return r
        













        # def cal(root):
            
        #     global flag2
        #     if not root: return None
        #     # print(root.val,p)
            
        #     if root.val == q.val:
        #         flag2 = 1
            
        #     li2.append(root.val)
        #     if not flag2:
        #         cal(root.left)
        #     if not flag2:
        #         cal(root.right)
                
        # cal(root)
        # print(li2)

