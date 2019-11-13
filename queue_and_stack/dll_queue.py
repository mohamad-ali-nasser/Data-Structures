import sys
# sys.path.append("C:\Users\mhdal\github\Data-Structures\doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.value = None
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.value = value
        self.storage.add_to_head(self.value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            self.size = 0
        else:
            value = self.storage.tail.value
            self.storage.remove_from_tail()
            self.size -= 1
            return value

    def len(self):
        return self.size
