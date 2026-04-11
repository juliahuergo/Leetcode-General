class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity  

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        value = self.dict[key]
        self.dict.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """       
        
        self.dict[key] = value
        self.dict.move_to_end(key)
        
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False) #we remove the first element, which is the LRU
