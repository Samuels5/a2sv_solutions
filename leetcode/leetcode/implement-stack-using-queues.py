class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return []
        

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()