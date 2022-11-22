Overview
========

The ``sll`` package provides a class for creating a singly linked list as
well as a function for converting a python list into a linked list.

Example usage:

.. code:: python

    import sll
    from sll import convert_to_linked_list
    mylist = [1, 2, 3, 4, 5]
    mylinkedlist = convert_to_linked_list(mylist)
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