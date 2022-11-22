Overview
========

The ``sll385`` package provides a class for creating a singly linked list as
well as a function for converting a python list into a linked list.

Example usage:

.. code:: python

    import sll385
    mylist = [1, 2, 3, 4, 5]
    mylinkedlist = sll385.convert_to_linked_list(mylist)
    mylinkedlist.printList()
    """
    1 2 3 4 5
    """
    mylinkedlist.addToHead(6)
    print(mylinkedlist.getVal(0))
    """
    6
    """
    mylinkedlist.deleteIndex(0)
    mylinkedlist.printList()
    """
    1 2 3 4 5
    """
    mylinkedlist.addToTail(6)
    mylinkedlist.printList()
    """
    1 2 3 4 5 6
    """