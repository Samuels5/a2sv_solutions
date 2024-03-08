class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if key in self.d and timestamp>=self.d[key][0][0]:
            val = bisect_right(self.d[key],(timestamp, '{'))
            return self.d[key][val-1][1]
        else:
            return ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)