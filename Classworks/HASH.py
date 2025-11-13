print(hash("Aльона"))
print(hash("Настя"))
print(hash("Максим"))

""""Simple hash table"""
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]

h = HashTable(10)
h.insert("Aльона", 39)
h.insert("Максим", 42)
print(h.get("Aльона"))