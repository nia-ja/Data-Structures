from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            storage_node = self.storage[key]
            self.cache.move_to_front(storage_node)
            return self.storage[key].value[1]
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            #retrieve key value node
            storage_node = self.storage[key]
            #update key value
            storage_node.value[1] = value
            #move node to top of stack
            self.cache.move_to_front(storage_node)
        else:
            #add data to cache and store it's reference in storage
            self.cache.add_to_head([key, value])
            self.storage[key] = self.cache.head
            if self.size >= self.limit:
                #remove the last value
                del self.storage[self.cache.tail.value[0]]
                self.cache.remove_from_tail()
            else:
                #cache wasn't full; increase size
                self.size += 1