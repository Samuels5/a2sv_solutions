class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        stack = []
        stack.append(k)
        while k != 1:
            stack.append(math.ceil(k/2))
            k  = math.ceil(k/2)

        zero = "01"
        one = "10"
        curr = zero[stack[-1] - 1]
        stack.pop()
        while len(stack) != 0:
            x = stack.pop()
            if x %2 == 0 and curr == '0':
                curr = zero[1]
            elif x %2 == 0 and curr == "1":
                curr = one[1]
            elif x %2 == 1 and curr == "0":
                curr = zero[0]
            else:
                curr = one[0]
        return int(curr)


       