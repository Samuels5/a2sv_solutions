class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.idx = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        r = []
        while self.idx < len(self.stream) and self.stream[self.idx] is not None:
            r.append(self.stream[self.idx])
            self.idx += 1
        return r