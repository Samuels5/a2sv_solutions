class MinStack:

    def __init__(self):
        self.stack = deque()
        self.q = deque()
        

    def push(self, val: int) -> None:
        if self.q and self.q[-1] >= val:
            self.q.append(val)
        elif not self.q:
            self.q.append(val)

        self.stack.append(val)
        
    def pop(self) -> None:
        poped = self.stack.pop()
        if poped == self.q[-1]:
            self.q.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.q[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()