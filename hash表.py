class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return default