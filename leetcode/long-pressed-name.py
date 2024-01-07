class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        while i<len(name) and j<len(typed):
            if name[i]==typed[j]:
                i+=1
                j+=1
                
            elif typed[j] ==typed[j-1] and j-1>=0:
                j+=1
            else: 
                break
        if i==len(name) and name[-1]==list(set(typed[j-1:]))[0] and len(list(set(typed[j-1:])))==1:
            return True
        else:
            return False
