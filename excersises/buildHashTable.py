'''
User Stories:

You should define a class named HashTable with a collection attribute 
initialized to an empty dictionary when a new instance of HashTable is created. 
The collection dictionary should store key-value pairs based on the hashed value of the key.

The HashTable class should have four instance methods: hash, add, remove, and lookup.

The hash method should:

Take a string as a parameter.
Return a hashed value computed as the sum of the Unicode (ASCII)
values of each character in the string. You can use the ord function for this computation.
The add method should:

Take two arguments representing a key-value pair, and compute the hash of the key.
Use the computed hash value as a key to store a dictionary containing
the key-value pair inside the collection dictionary.
If multiple keys produce the same hash value, their key-value pairs
should be stored in the existing nested dictionary under the same hash value.
The remove method should:

Take a key as its argument and compute its hash.
Confirm if the key exists in the collection.
Remove the corresponding key-value pair from the hash table.
If the key does not exist in the collection, it should not raise an error
or remove anything.
The lookup method should:

Take a key as its argument.
Compute the hash of the key, and return the corresponding 
value stored inside the hash table.
If the key does not exist in the collection, it should return None.
 
'''

class HashTable:
    def __init__(self):
        self.collection = {}
        
    def hash(self, key):
        hashed_value = 0
        for i in key:
            hashed_value += ord(i)
        return hashed_value
    
    def add(self, key, value):
        new_key = self.hash(key)
        if new_key in self.collection:
            self.collection[new_key].update({key: value})
        else:
            self.collection[new_key] = {key: value}
    def remove(self, key):
        prim_key = self.hash(key)
        if prim_key in self.collection:
            if key in self.collection[prim_key]:
                del self.collection[prim_key][key]
                if not self.collection[prim_key]:
                    del self.collection[prim_key]
    def lookup(self,key):
        prim_key = self.hash(key)
        if prim_key in self.collection:
            if key in self.collection[prim_key]:
                return self.collection[prim_key][key]
        else:
            return None
