class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        idx = bisect_left(self.dict[key], (timestamp+1, "")) - 1  #first pos 
        print(idx)
        if idx >= 0 and idx < len(self.dict[key]) and self.dict[key][idx][0] <= timestamp:
            return self.dict[key][idx][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
