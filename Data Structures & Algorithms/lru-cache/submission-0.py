class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = OrderedDict()


    def get(self, key: int) -> int:
        val = self.dic.get(key, -1)
        if val != -1:
            self.dic.move_to_end(key)
        return val

        

    def put(self, key: int, value: int) -> None:
        val = self.dic.get(key, -1)
        if val != -1:
            self.dic.move_to_end(key)
        
        self.dic[key] = value
        
        if len(self.dic) > self.cap:
            self.dic.popitem(last = False)

        
