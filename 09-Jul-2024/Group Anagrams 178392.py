# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for val in strs:
            a[''.join(sorted(list(val)))].append(val)

        t = []
        for val in a.values():
            t.append(sorted(val))

        return t