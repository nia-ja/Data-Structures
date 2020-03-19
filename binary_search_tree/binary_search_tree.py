import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# Tree Node
class BinarySearchTree:
    def __init__(self, value):
        self.value = value # value of current node
        self.left = None # Binary Search Tree (left -> smaller)
        self.right = None # Binary Search Tree (right -> bigger)

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node
        # if smaller, go left
        # if bigger, go right
        # repeat, if neccessary -> recursion?

        # if no node to go to, (either left or right) (i.e, left or right is None) -> base case
        # make the new node at that spot

        ## if no node.left AND value is less than node.value OR no node.right and value greater than node.value

        #current node has no value
        if not self.value:
            self.value = value
            return
        #value is less than current node and no left subtree exists
        #initiate a left subtree with value
        elif value < self.value and not self.left:
            self.left = BinarySearchTree(value)
        #value is less than current node and left subtree exists
        #run insert on the left subtree
        elif value < self.value and self.left:
            self.left.insert(value)
        #value is greater than current node and no right subtree exists
        #initiate a right subtree with value
        elif value >= self.value and not self.right:
            self.right = BinarySearchTree(value)
        #value is greater than current node and right subtree exists
        #run insert on the right subtree
        elif value > self.value and self.right:
            self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        # compare value to the current node value
        # if smaller, go left
        # if bigger, go right
        # repeat, if neccessary -> recursion
        # if equal, return True!

        # if smaller, but we cant go left, return false
        # if bigger, but we cant go right, return false

    # Return the maximum value found in the tree
    def get_max(self):
        # all the way to the right
        # if there's nowhere to go -> we hit the base case (max value)
        if self.right is None:
            return self.value
        # if there is a way to the right
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # when there's nowhere to go, just call the node itself -> base case
        cb(self.value)
        # if we can go left
        if self.left is not None:
            self.left.for_each(cb)
        # if we can go right
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
