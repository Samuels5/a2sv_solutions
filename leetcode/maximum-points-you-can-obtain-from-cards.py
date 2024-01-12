class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        arr=[]
        arr.extend(cardPoints[-k:])
        arr.extend(cardPoints[:k])
        sumi=sum(arr[:k])
        maxi=sumi
        for num in range(len(arr)-k):
            sumi+=arr[num+k]
            sumi-=arr[num]
            maxi=max(sumi,maxi)

        return maxi