class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.left = 0
        self.right = -1
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.right - self.left + 1 < self.k:
            self.queue.append(value)
            self.right += 1
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        if self.left <= self.right:
            self.left += 1
            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.left]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.right]
        

    def isEmpty(self) -> bool:
        if self.left>self.right:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.right - self.left + 1 == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()