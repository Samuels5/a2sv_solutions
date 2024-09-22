# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        
        for val in arr:
            pre.append(pre[-1]^val)
            
        ans = []
        for val in queries:
            ans.append(pre[val[0]]^pre[val[1]+1])

        return ans