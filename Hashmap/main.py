# Hashmap implementation in Python

class HashMap:
    INITIAL_SIZE = 1<<4 # 16
    MAXIMUM_CAPACITY = 1<<30 # 1073741824 or 2^30
    LOAD_FACTOR = 0.75

    def __init__(self, size=INITIAL_SIZE):
        if size == self.INITIAL_SIZE:
            self.size = size
        else:
            self.size = self.get_table_size(size)
        
        self.count = 0 # Number of key-value pairs in the hash table
        self.table = [None] * self.size  # Initialize the hash table with None

    def get_table_size(self, capacity):
        """
        If the capacity is not a power of 2, then return the next power of 2
        """
        n = capacity - 1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        return 1 if n < 0 else min(n + 1, self.MAXIMUM_CAPACITY)
    
    def _hash(self, key):
        """
        Hash function to calculate the index of the key for the hash table
        """
        return hash(key) % self.size

    def resize(self):
        """
        Resize the hash table when the count of elements exceeds the threshold or 75%
        """
        if self.size >= self.MAXIMUM_CAPACITY:
            raise Exception("Hash table is full")
        
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        # self.count = 0

        for bucket in old_table:
            if bucket:
                for k, v in bucket:
                    self.put(k, v)

    
    def put(self, key, value):
        """
        Insert a key-value pair into the hash table
        """
        # Resize the hash table if the elements exceed the load factor
        if self.count / self.size > self.LOAD_FACTOR:
            self.resize()

        hashIdx = self._hash(key)

        if self.table[hashIdx] is None:
            self.table[hashIdx] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[hashIdx]):
                if k == key:  # Handle collision by appending to the same bucket
                    self.table[hashIdx][i] = (key, value)
                    return
            self.table[hashIdx].append((key, value))  # Add a new key-value pair to the bucket
        
        self.count += 1

    def get(self, key):
        """
        Retrieve the value of the key from the hash table
        """
        hashIdx = self._hash(key)

        if self.table[hashIdx] is not None:
            for k, v in self.table[hashIdx]:
                if k == key:
                    return v
                
        return None

    def remove(self, key):
        """
        Remove the key-value pair from the hash table
        """
        hashIdx = self._hash(key)

        if self.table[hashIdx] is not None:
            for i, (k, v) in enumerate(self.table[hashIdx]):
                if k == key:
                    del self.table[hashIdx][i]
                    self.count -= 1
                    return True
        return False

    def __str__(self):
        """
        String representation of the hash table
        """
        mp = []
        for bucket in self.table:
            if bucket:
                for k, v in bucket:
                    mp.append(f'{k}: {v}')
        return '{' + ', '.join(mp) + '}'    

        # return '{' + ', '.join(f'{k}: {v}' for bucket in self.table if bucket for k, v in bucket) + '}'
    

if __name__ == "__main__":
    hmap = HashMap(5)
    hmap.put("name", "John Doe")
    hmap.put("age", 30)
    hmap.put("city", "New York")
    hmap.put("country", "USA")
    hmap.put("country", "India")
    hmap.put("gender", "Male")
    hmap.put("email", "johndoe@gmail.com")

    print(hmap)

    print(hmap.get("name"))
    print(hmap.get("age"))

    hmap.remove("city")
    print(hmap)
    print(hmap.get("city"))  


# Output
"""
{gender: Male, name: John Doe, city: New York, country: India, email: johndoe@gmail.com, age: 30}
John Doe
30
{gender: Male, name: John Doe, country: India, email: johndoe@gmail.com, age: 30}
None
"""