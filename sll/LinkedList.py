"""Classes that implement a linked list and its nodes. A function is also provided to convert a Python list to a linked list."""
class Node:
    """
    Linked List Node.
    
    Creates a Node.
    
    :param val: The value of the node.
    
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """
    Singly Linked List.
    
    Creates a linked list of nodes.

    """

    def __init__(self):
        self.head = None
        self.size = 0

    def getVal(self, index):
        """
        Gets the value at an index.
        
        :param index: int, the index of the value to get.
        
        """
        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return curr.val

    def addToHead(self, val):
        """
        Add a value at the head.
        
        :param val: The value to add at the head.
        
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addToTail(self, val):
        """
        Add a value to the tail.
        
        :param val: The value to add at the tail.
        
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a value at a specific index.
        
        :param index: int, the index where to add value.
        :param val: The value to add to the list.
        
        """
        if index < 0 or index > self.size:
            return -1
        if index == 0:
            node = Node(val)
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
        self.size += 1

    def deleteIndex(self, index):
        """
        Delete a value at a specific index.
        
        :param index: int, the index of the value to delete.
        
        """
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        
    def printList(self):
        """
        Print all the elements in the linked list.
    
        """
        curr = self.head
        while curr is not None:
            print(curr.val, end=" ")
            curr = curr.next
        print()



def convert_to_linked_list(arr):
    """
    Converts a Python list to a linked list.
    :param arr: array, Python list.
    """
    linked_list = LinkedList()
    for i in range(len(arr)):
        linked_list.addToTail(arr[i])
    return linked_list