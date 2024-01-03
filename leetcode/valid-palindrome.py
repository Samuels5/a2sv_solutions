class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i.isnumeric():
                arr.append(i)
            if i.isalpha():
                x=i.lower()
                arr.append(x)
        sr=''.join(arr)
        if arr[::]==arr[::-1]:
            return True
        return False