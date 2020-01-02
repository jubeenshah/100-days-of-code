import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except:
            return -1
        

    def put(self, key: int, value: int) -> None:
        try:
            self.cache.pop(key)
        except:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)