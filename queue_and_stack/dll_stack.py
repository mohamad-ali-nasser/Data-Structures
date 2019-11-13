from doubly_linked_list import DoublyLinkedList
import sys
# sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.value = value
        self.storage.add_to_tail(self.value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            self.size = 0
        else:
            v = self.storage.tail.value
            self.storage.remove_from_tail()
            self.size -= 1
            return v

    def len(self):
        return self.size
