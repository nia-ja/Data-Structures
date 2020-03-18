import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# FIRST in (add to the head) -> LAST out (remove from the head)
# stack of pancakes
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # add
    def push(self, value):
        self.size += 1
        # first in
        self.storage.add_to_head(value)

    # delete
    def pop(self):
        # check for no values
        if self.size == 0:
            return None
        else:
            self.size -= 1
            # last out
            return self.storage.remove_from_head()

    def len(self):
        return self.size
