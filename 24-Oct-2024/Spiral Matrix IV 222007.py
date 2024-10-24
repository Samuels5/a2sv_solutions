# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = []
        for row in range(m):
            new = []
            for col in range(n):
                new.append(-1)
            arr.append(new)
            
        d = 0 if n >1 else 1
        row, col, l, t = 0, 0, 0, 1
        cur = head
        b = m - 1
        r = n - 1

        while cur:
            arr[row][col] = cur.val
            # print(arr, row, col, l, r , b, t, d)
            # print(cur.val,arr)
            cur = cur.next
            if not cur:
                break
            if d == 0:
                col += 1
            if d == 1:
                row += 1
            if d == 2:
                col -= 1
            if d == 3:
                row -= 1

            if col >= r and d == 0:
                d += 1
                r -= 1

            if row >= b and d == 1:
                d += 1
                b -= 1

            if col <= l and d == 2:
                d += 1
                l += 1

            if row <= t and d == 3:
                d += 1
                t += 1

            # d += 1
            if d >= 4:
                d = 0

        return arr
