class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ''
        li = list(palindrome)
        mid = -1
        if len(palindrome)%2==1:
            mid = len(palindrome)//2
        for idx,val in enumerate(li):
            if mid== idx:
                continue
            if idx == len(li)-1:
                li[idx] = 'b'
                return ''.join(li)
            if val != 'a':
                li[idx] = 'a'
                return ''.join(li)
            

        
        