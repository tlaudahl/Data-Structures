import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If value < node.value go left
        if value < self.value:
            # if something is there already
            if self.left:
                # recurse to the left
                self.left.insert(value)
            # if not
            else:
                self.left = BinarySearchTree(value)
                # insert left
        # If value is >= node.value look right
        if value >= self.value:
            # if something is there already
            if self.right:
                # recurse to the right
                self.right.insert(value)
            # if not
            else:
                self.right = BinarySearchTree(value)
            


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Call cb on self.value
        cb(self.value)
        # if left
        if self.left:
            # call for_each
            self.left.for_each(cb)
        # if right
        if self.right:
            # call for_each
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # initialize a queue
        queue = Queue()
        # push root to queue
        queue.enqueue(node)
        # while queue is not empty
        while queue.len() > 0:
        # pop top item out of queue into temp
            current_node = queue.dequeue()
        # DO THE THING
            print(current_node.value)
        # if current_node has right put right into queue
            if current_node.left:
                queue.enqueue(current_node.left)
        # if current_node has left put into queue
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Initialize a stack
        stack = Stack()
        # Push root to stack
        stack.push(node)
        # while stack not empty
        while stack.len() > 0:
        # pop top item out of stack into temp
            current_node = stack.pop()
            print(current_node.value)
        # if temp has right put into stack
            if current_node.right:
                stack.push(current_node.right)
        # if temp has left put into stack
            if current_node.left:
                stack.push(current_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.dft_print(bst)
bst.in_order_print(bst)