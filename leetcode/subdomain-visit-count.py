class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d=defaultdict(int)
        for cp in cpdomains:
            num,domain = cp.split()
            num=int(num)
            domains=domain.split('.')
            domains[:]=domains[::-1]
            sting1=''
            for word in domains:
                if sting1=='':
                    sting1=word
                else:
                    sting1= word + '.' + sting1
                d[sting1]+=num
        arr=[]
        for dom,nums in d.items():
            arr.append(str(nums)+' '+dom)

        
        return arr