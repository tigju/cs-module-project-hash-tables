class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        curStr = ""
        curr = self.head
        while curr:
            curStr += f"{str(curr.value)} -> "
            curr = curr.next
        return curStr
    
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None

    def delete(self, key):
        curr = self.head

        # if node with value is a head node
        if curr.key == key:
            self.head = curr.next
            return curr.value

        # general case of deleting internal node
        prev = curr
        curr = curr.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                return curr.value
            else:
                prev = curr
                curr = curr.next

        return f"key is not found"

    def insert_at_head_or_overwrite(self, node):
        existing_node = self.find(node.value)
        if existing_node is None:
            self.insert_at_head(node)
        else:
            existing_node.value = node.value
        

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):

        self.capacity = capacity    
        self.storage = [None for i in range(self.capacity)]
        self.count = 0

    def __repr__(self):
        curStr = ""
        curr = self.storage
        for i, v in enumerate(curr):
            curStr += f"index: {str(i)} value: {str(v)} ;"
        return curStr

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # basicaly the length of the array
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # number of items devided by number or slots in array
        return self.count/self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        enc = key.encode()
        hsh = 5381
        for char in enc:
            hsh = ((hsh << 5) + hsh) + char
        
        return hsh & 0xFFFFFFFF
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = HashTableEntry(key, value)
        list_position = self.storage[index]
        ll = LinkedList() 
        if list_position == None:
            ll = LinkedList()
            ll.insert_at_head(node)
            self.storage[index] = ll 
            self.count += 1   
        else:
            if list_position.find(key) is None:
                self.count += 1
            list_position.insert_at_head_or_overwrite(node)
            
          
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        ll = self.storage[index]
        if ll.find(key) is not None:
            self.count -= 1
        return ll.delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        ll = self.storage[index]
        return ll.find(key)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass



'''
Hashtable no collisions Day 1
'''


# class HashTableEntry:
#     """
#     Linked List hash table key/value pair
#     """

#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None


# # Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8


# class HashTable:
#     """
#     A hash table that with `capacity` buckets
#     that accepts string keys
#     Implement this.
#     """

#     def __init__(self, capacity):

#         self.capacity = capacity
#         self.storage = [None for i in range(self.capacity)]

#     def get_num_slots(self):
#         """
#         Return the length of the list you're using to hold the hash
#         table data. (Not the number of items stored in the hash table,
#         but the number of slots in the main list.)
#         One of the tests relies on this.
#         Implement this.
#         """
#         # Your code here
#         pass

#     def get_load_factor(self):
#         """
#         Return the load factor for this hash table.
#         Implement this.
#         """
#         # Your code here
#         pass

#     def fnv1(self, key):
#         """
#         FNV-1 Hash, 64-bit
#         Implement this, and/or DJB2.
#         """
#         # Your code here
#         pass

#     def djb2(self, key):
#         """
#         DJB2 hash, 32-bit
#         Implement this, and/or FNV-1.
#         """
#         # Your code here
#         enc = key.encode()
#         hsh = 5381
#         for char in enc:
#             hsh = ((hsh << 5) + hsh) + char

#         return hsh & 0xFFFFFFFF

#     def hash_index(self, key):
#         """
#         Take an arbitrary key and return a valid integer index
#         between within the storage capacity of the hash table.
#         """
#         #return self.fnv1(key) % self.capacity
#         return self.djb2(key) % self.capacity

#     def put(self, key, value):
#         """
#         Store the value with the given key.
#         Hash collisions should be handled with Linked List Chaining.
#         Implement this.
#         """
#         # Your code here
#         index = self.hash_index(key)

#         self.storage[index] = value

#     def delete(self, key):
#         """
#         Remove the value stored with the given key.
#         Print a warning if the key is not found.
#         Implement this.
#         """
#         # Your code here
#         index = self.hash_index(key)
#         if self.storage[index]:
#             self.storage[index] = None
#         else:
#             return f"key is not found"

#     def get(self, key):
#         """
#         Retrieve the value stored with the given key.
#         Returns None if the key is not found.
#         Implement this.
#         """
#         # Your code here
#         index = self.hash_index(key)
#         if self.storage[index]:
#             return self.storage[index]
#         else:
#             return None

#     def resize(self, new_capacity):
#         """
#         Changes the capacity of the hash table and
#         rehashes all key/value pairs.
#         Implement this.
#         """
#         # Your code here
#         pass


'''
end of hashtable no collision
'''

if __name__ == "__main__":
#     # ht = HashTable(8)

#     # ht.put("line_1", "'Twas brillig, and the slithy toves")
#     # ht.put("line_2", "Did gyre and gimble in the wabe:")
#     # ht.put("line_3", "All mimsy were the borogoves,")
#     # ht.put("line_4", "And the mome raths outgrabe.")
#     # ht.put("line_5", '"Beware the Jabberwock, my son!')
#     # ht.put("line_6", "The jaws that bite, the claws that catch!")
#     # ht.put("line_7", "Beware the Jubjub bird, and shun")
#     # ht.put("line_8", 'The frumious Bandersnatch!"')
#     # ht.put("line_9", "He took his vorpal sword in hand;")
#     # ht.put("line_10", "Long time the manxome foe he sought--")
#     # ht.put("line_11", "So rested he by the Tumtum tree")
#     # ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     # for i in range(1, 13):
#     #     print(ht.get(f"line_{i}"))

#     # # Test resizing
#     # old_capacity = ht.get_num_slots()
#     # ht.resize(ht.capacity * 2)
#     # new_capacity = ht.get_num_slots()

#     # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # # Test if data intact after resizing
#     # for i in range(1, 13):
#     #     print(ht.get(f"line_{i}"))

#     # print("")

#     # hat = HashTable(8)
#     # print(hat.hash_index("cat"))
#     # print(hat.hash_index("world"))
#     # print(hat.storage)
#     # print(hat.put("cat", "meow"))
#     # print(hat.storage)
#     # print(hat.put("dog", "woof"))
#     # print(hat.storage)
#     # print(hat.put("cat", "purr"))
#     # print(hat.storage)
#     # print(hat.put("world", "world value"))
#     # print(hat.storage)
#     # print(hat.put("hello", "hello value"))
#     # print(hat.storage)
#     # print(hat.count)
#     # my  = hat.get("cat")
#     # rem = hat.delete("hello")
#     # print(rem.value)
#     # print(hat.storage)
#     # rem1 = hat.delete("world")
#     # print(rem1.value)
#     # print(hat.storage)
#     # print(hat.get_num_slots())
    
#     # print(hat)
#     # print(hat.count)
#     # print(hat.get_load_factor())
#     # ll = LinkedList()
#     # ll.insert_at_head_or_overwrite(HashTableEntry("cat", "meow"))
#     # ll.insert_at_head_or_overwrite(HashTableEntry("dog", "woof"))
#     # print(ll)
#     # ll.insert_at_head_or_overwrite(HashTableEntry("cat", "purr"))
    
#     # print(ll.find('woof'))

#     # print(ll.delete('meow'))

#     # print(ll)

    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    print(ht.get("key-0"))

    ht.put("key-0", "new-val-0")
    print(ht.get("key-0"))
