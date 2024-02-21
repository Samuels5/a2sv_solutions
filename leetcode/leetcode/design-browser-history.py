class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = homepage
        self.li = [homepage]
        self.point = 0

    def visit(self, url: str) -> None:
        self.li = self.li[:self.point+1]
        self.li.append(url)
        self.point += 1

    def back(self, steps: int) -> str:
        for num in range(steps):
            if self.point>0:
                self.point -= 1

        return self.li[self.point]

    def forward(self, steps: int) -> str:
        for val in range(steps):
            if self.point < len(self.li)-1:
                self.point += 1
        
        return self.li[self.point]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)