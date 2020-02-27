import sys
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Push is an array method to add to a list so we add + 1 to the size
        self.size += 1
        # Then we add that value to the head
        self.storage.add_to_head(value)

    def pop(self):
        # Can't remove an element if no elements exist
        if self.size == 0:
            return None
        else:
            self.size -= 1
            popped = self.storage.remove_from_head()
        return popped

    def len(self):
        # Our size variable is the same as the length
        return self.size
