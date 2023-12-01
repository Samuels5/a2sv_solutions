class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        a=[]
        while True:
            if i==j:
                a.append(word1[i])
                i+=1
            elif i>j:
                a.append(word2[j])
                j+=1
            if i>len(word1)-1:
                a.append(word2[j:])
                break
            if j>len(word2)-1:
                a.append(word1[i:])
                break
        print(a)
        print(word1,word2)
        return ''.join(a)