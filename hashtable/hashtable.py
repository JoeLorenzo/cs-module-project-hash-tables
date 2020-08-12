class Node:
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key=None, value=None):
        self.head = None

    def add_to_head(self, key, value):
        
        new_node = Node(key, value)
        if self.head == None:
            self.head = new_node
        
        else:
            # new node should point to current head
            new_node.next_node = self.head
            # new head equals to new node
            self.head = new_node

        
    def contains(self, key):
        # check if list is empty first, if so return false
        if self.head is None:
            return False
        # loop through each node until we see the key or we could not go further
        current_node = self.head  
        while current_node is not None:
            if current_node.key == key:
                return True
            # otherwise go to the next node
            current_node = current_node.next_node
        return False


    def replace_value(self, key, value):
        # check if list is empty first, if so return false
        if self.head is None:
            return False
        # loop through each node until we see the key or we could not go further
        current_node = self.head  
        while current_node is not None:
            if current_node.key == key:
                current_node.value = value 
            # otherwise go to the next node
            current_node = current_node.next_node
        return False



        


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.hash_table = capacity * [HashTableEntry()]
        self.items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """

        return len(self.hash_table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.items / self.get_num_slots()


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
   
        hash = 5381
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash


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
        # find the index of the key
        i = self.hash_index(key)
        # check if key alrady exists
        # if key does not exist then add key and values to the head
        if self.hash_table[i].contains(key) == False:
            # increment item counter 
            self.item =+ 1
            return self.hash_table[i].add_to_head(key, value)
        # else replace the value for the key
        else:
            return self.hash_table[i].replace_value(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        i = self.hash_index(key)

        if self.hash_table[i] == None:
            print(f"key: {key} Not Found")

        elif self.hash_table[i] != None:
            print(f"Deleting, value: {repr(self.hash_table[i])}")

        self.hash_table[i] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)

        if self.hash_table[i] == None:
            print("Key Not Found")

        elif self.hash_table[i] != None:
            return self.hash_table[i]




    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)
    # print(ht.capacity)
    # print(ht.hash_table[0].head)

    print(f"number of buckets:  {ht.get_num_slots()}")
    # print(ht.hash_index("Twas brillig, and the slithy toves"))

    ht.put("line_1", "Twas brillig, and the slithy toves")
    ht.put("line_1", "Twas the night before Christmas")
    print(ht.hash_table[0].head.value)
    print(ht.hash_table[0].head.key)
    # print(ht.hash_table[0].head.next_node.value)

    print(f"number of items {ht.items}")


    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    ht.get("line_12")

    ht.delete("line_12")
    ht.delete("line_12")
    ht.get("line_12")


    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
