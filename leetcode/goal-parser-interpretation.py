class Solution:
    def interpret(self, command: str) -> str:
        i=0
        a=[]
        while i<len(command):
            if command[i]=='G':
                a.append('G')
                i+=1
            elif command[i]=='(' and command[i+1]==')':
                a.append('o')
                i+=1
            elif command[i]=='a': #and command[i]=='l':
                a.append('al')
                i+=1
            elif command[i]==')'or'l':
                i+=1
        return ''.join(a)