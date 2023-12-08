class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for num in nums:
            if num<0:
                negative.append(num)
            else:
                positive.append(num)
        re = []
        for number in range(len(positive)):
            re.append(positive[number])
            re.append(negative[number])
        return re