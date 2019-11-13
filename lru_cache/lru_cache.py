from doubly_linked_list import ListNode, DoublyLinkedList

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
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        self.key = key
        current_key = self.storage.head
        value = None
        # done = None
        while current_key is not None:
                print('nowhtev')
                if self.key in current_key.value:
                    print(current_key.value[self.key])
                    value = current_key.value[self.key]
                    self.storage.move_to_front(current_key)
                    return value
                    # done = 1
                current_key = current_key.next
        return value

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
        self.key = key
        self.value = value
        current_key = self.storage.head
        done = None
        if self.limit == 0:
            self.storage.remove_from_tail()
            self.storage.add_to_head({self.key: self.value})
        else:
            while current_key is not None:
                if self.key in current_key.value:
                    # current_key.value[self.key] = self.value
                    self.storage.delete(current_key)
                    self.storage.add_to_head({self.key: self.value})
                    done = 1
                current_key = current_key.next
            if done is None:
                self.storage.add_to_head({self.key: self.value})
                self.limit -= 1
