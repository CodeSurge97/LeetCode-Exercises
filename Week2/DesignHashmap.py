class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None] * 10000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_index = hash(key) % 10000
        if self.map[hash_index] is None:
            self.map[hash_index] = Node(key, value)
        else:
            previous = None
            start = self.map[hash_index]
            while start is not None:
                if start.key == key:
                    start.value = value
                    return
                previous = start
                start = start.next
                
            previous.next = Node(key, value)
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_index = hash(key) % 10000
        start = self.map[hash_index]
        while start is not None:
            if start.key == key:
                return start.value
            start = start.next
        return -1