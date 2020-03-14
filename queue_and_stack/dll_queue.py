import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# FIRST in (add to the head) -> FIRST out (remove from the tail)
# waiting in line
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # add
    def enqueue(self, value):
        self.size += 1
        # first in
        self.storage.add_to_head(value)

    # delete
    def dequeue(self):
        # check for no values
        if self.size == 0:
            return None
        else:
            self.size -= 1
            # first out
            return self.storage.remove_from_tail()


    def len(self):
        return self.size