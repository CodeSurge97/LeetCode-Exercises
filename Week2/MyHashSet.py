class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # n is the size of the set and m is the capacity of the set
        self.n = 0
        self.m = 4
        self.load_factor = self.n / self.m
        self.table = [[] for i in range(self.m)]
        
    
    def rehash_inc(self):
        # double the size of the array
        self.m *= 2
        newtable = [[] for i in range(self.m)]
        # rehash into new table
        for i in self.table:
            for j in i:
                newtable[self.prehash(j)].append(j)
        self.table = newtable
        
    def rehash_dec(self):
        self.m //= 2
        newtable = [[] for i in range(self.m)]
        # rehash into new table
        for i in self.table:
            for j in i:
                newtable[self.prehash(j)].append(j)
        self.table = newtable
    
    def prehash(self,num):
        # we use the simple division method of hashing
        # universal hashing can also be used
        return ((17205624*num + 28676040) % 86028121) % self.m
        

    def add(self, key: int) -> None:
        # if already contains just return
        if self.contains(key):
            return
        if self.load_factor > 1:
            self.rehash_inc()
        self.table[self.prehash(key)].append(key)
        # update the n and load factor
        self.n += 1
        self.load_factor = self.n / self.m

    def remove(self, key: int) -> None:
        if self.load_factor < 0.25:
            self.rehash_dec()
        # just remove the particular element if found
        for i in range(len(self.table[self.prehash(key)])):
            if self.table[self.prehash(key)][i] == key:
                self.table[self.prehash(key)].pop(i)
                self.n -= 1
                self.load_factor = self.n/self.m
                return
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for i in range(len(self.table[self.prehash(key)])):
            if self.table[self.prehash(key)][i] == key:
                return True
        return False