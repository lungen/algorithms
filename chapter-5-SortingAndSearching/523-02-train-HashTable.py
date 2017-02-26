class Hash:
    def __init__(self):
        self.size = 11
        self.slots = self.size * [None]
        self.data = self.size * [None]

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def __setitem__(self, key, data):
        return self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, data):
        hashValue = self.hash_function(key)

        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data  # replace
            else:
                next_slot = self.rehash(hashValue)

                while self.slots[next_slot] is not None \
                        and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def get(self, key):
        start_slot = self.hash_function(key)
        stop, data = False, None

        if self.slots[start_slot] == key:
            data = self.data[start_slot]
        else:
            newSlot = self.rehash(start_slot)

            while self.slots[newSlot] != key and not stop:
                newSlot = self.rehash(newSlot)
                if newSlot == start_slot:
                    stop = True

            if self.slots[newSlot] == key:
                data = self.data[newSlot]

        return data


H = Hash()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

print(H.slots)
print(H.data)
print(H[54])
print(H[6])
