# sll385

## Description

This python package provides a function to convert a regular list into a linked list. It also provides several methods to manipulate the linked list.

## Installation

pip install sll385

https://pypi.org/project/sll385/

## Documentation

https://tanneroates2.github.io/sll385/

## Examples

```python
import sll385 as sll
mylist = [1, 2, 3, 4, 5]
mylinkedlist = sll.convert_to_linked_list(mylist)
mylinkedlist.printList()
"""
1 2 3 4 5
"""
mylinkedlist.addToHead(0)
print(mylinkedlist.getVal(0))
"""
0
"""
mylinkedlist.deleteIndex(2)
mylinkedlist.printList()
"""
0 1 3 4 5
"""
mylinkedlist.addToTail(6)
mylinkedlist.printList()
"""
0 1 3 4 5 6
"""
mylinkedlist.addAtIndex(2, 2)
mylinkedlist.printList()
"""
0 1 2 3 4 5 6
"""
'''
