class RecentCounter:

    def __init__(self):
        self.dq = deque()
        

    def ping(self, t: int) -> int:
        if self.dq:
            if t - self.dq[0] < 3000:
                self.dq.append(t) 
            else:
                while self.dq and t - self.dq[0] > 3000:
                    self.dq.popleft()
                self.dq.append(t)
        else:
            self.dq.append(t)

        return len(self.dq)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)