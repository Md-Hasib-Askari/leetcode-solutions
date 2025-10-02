class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.db: self.db[key].append((timestamp, value))
        else: self.db[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        
        arr = self.db[key]
        l, r = 0, len(arr)-1
        res = -1
        while l <= r:
            m = l + (r-l) // 2
            if arr[m][0] <= timestamp:
                res = m
                l = m + 1
            else: r = m - 1

        return "" if res == -1 else arr[res][1]


if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar1", 1)
    param_1 = obj.get("foo", 1)
    print(f"Input: {('foo', 'bar1', 1)}")
    print(f"Output: {param_1}")
    print("-" * 20)

    obj.set("foo", "bar2", 2)
    param_2 = obj.get("foo", 3)
    print(f"Input: {('foo', 'bar2', 2)}")
    print(f"Output: {param_2}")
    print("-" * 20)
