class Solution:
    def reverseWords(self, s: str) -> str:
        s1=s.split(' ')
        s2=s1[::-1]
        s3=[]
        for i in s2:
            if i == '':
                continue
            else:
                s3.append(i)

        return ' '.join(s3)