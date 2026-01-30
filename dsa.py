class Node:
    """ArithmeticError: Raised when an error occurs in numeric calculations."""

    data=None
    next_node=None

    def __init__(self, data):
        self.data=data
    
    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        
        return " -> ".join(nodes)
        

class LinkedList:
    """
    Singly Linked List 
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes(O)n times
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count
    def add(self, data):
        """
        Adds new Node conotaining data at head of the list
        Takes O(1) time

        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node