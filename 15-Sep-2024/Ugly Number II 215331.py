# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def __init__(self):
        self.arr = [1]
        i = 0
        st = set()
        while len(self.arr) <5000:
            if self.arr[i]*2 not in st:
                st.add(self.arr[i]*2)
                self.arr.append(self.arr[i]*2)
            if self.arr[i]*3 not in st:
                st.add(self.arr[i]*3)
                self.arr.append(self.arr[i]*3)
            if self.arr[i]*5 not in st:
                st.add(self.arr[i]*5)
                self.arr.append(self.arr[i]*5)
            i += 1
        self.arr.sort()

    def nthUglyNumber(self, n: int) -> int:
        # print(self.arr)
        return self.arr[n-1]