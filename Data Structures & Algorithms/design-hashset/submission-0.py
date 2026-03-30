class MyHashSet:

    def __init__(self):
        self.dat = [False] * 10000001

    def add(self, key: int) -> None:
        self.dat[key] = True

    def remove(self, key: int) -> None:
        self.dat[key] = False

    def contains(self, key: int) -> bool:
        return self.dat[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)