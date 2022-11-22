"""pytest unit tests for the LinkedList module"""
import sll
from sll import convert_to_linked_list

def testNode():
    """test the Node class"""
    node = sll.Node(1)
    assert node.val == 1
    assert node.next == None

def testConversion():
    """test the conversion from list to LinkedList"""
    lst = [1, 2, 3, 4, 5]
    ll = sll.convert_to_linked_list(lst)
    assert ll.size == len(lst)
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 3
    assert ll.head.next.next.next.val == 4
    assert ll.head.next.next.next.next.val == 5
    assert ll.head.next.next.next.next.next == None
    
def testGetVal():
    """test the getVal method"""
    lst = [1, 2, 3, 4, 5]
    ll = sll.convert_to_linked_list(lst)
    assert ll.getVal(0) == 1
    assert ll.getVal(1) == 2
    assert ll.getVal(2) == 3
    assert ll.getVal(3) == 4
    assert ll.getVal(4) == 5
    assert ll.getVal(5) == -1
    assert ll.getVal(-1) == -1
    
def testAddToHead():
    """test the addToHead method"""
    lst = [1, 2, 3, 4, 5]
    ll = sll.convert_to_linked_list(lst)
    ll.addToHead(0)
    assert ll.size == 6
    assert ll.head.val == 0
    assert ll.head.next.val == 1
    assert ll.head.next.next.val == 2
    assert ll.head.next.next.next.val == 3
    assert ll.head.next.next.next.next.val == 4
    assert ll.head.next.next.next.next.next.val == 5
    assert ll.head.next.next.next.next.next.next == None
    
def testAddToTail():
    """test the addToTail method"""
    lst = [1, 2, 3, 4, 5]
    ll = sll.convert_to_linked_list(lst)
    ll.addToTail(6)
    assert ll.size == 6
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 3
    assert ll.head.next.next.next.val == 4
    assert ll.head.next.next.next.next.val == 5
    assert ll.head.next.next.next.next.next.val == 6
    assert ll.head.next.next.next.next.next.next == None
    
def testAddAtIndex():
    """test the addAtIndex method"""
    lst = [1, 2, 3, 4, 5]
    ll = sll.convert_to_linked_list(lst)
    ll.addAtIndex(0, 0)
    assert ll.size == 6
    assert ll.head.val == 0
    assert ll.head.next.val == 1
    assert ll.head.next.next.val == 2
    assert ll.head.next.next.next.val == 3
    assert ll.head.next.next.next.next.val == 4
    assert ll.head.next.next.next.next.next.val == 5
    assert ll.head.next.next.next.next.next.next == None
    ll.addAtIndex(6, 6)
    assert ll.size == 7
    assert ll.head.val == 0
    assert ll.head.next.val == 1
    assert ll.head.next.next.val == 2
    assert ll.head.next.next.next.val == 3
    assert ll.head.next.next.next.next.val == 4
    assert ll.head.next.next.next.next.next.val == 5
    assert ll.head.next.next.next.next.next.next.val == 6
    assert ll.head.next.next.next.next.next.next.next == None
    ll.addAtIndex(3, 3)
    assert ll.size == 8
    assert ll.head.val == 0
    assert ll.head.next.val == 1
    assert ll.head.next.next.val == 2
    assert ll.head.next.next.next.val == 3
    assert ll.head.next.next.next.next.val == 3
    assert ll.head.next.next.next.next.next.val == 4
    assert ll.head.next.next.next.next.next.next.val == 5
    assert ll.head.next.next.next.next.next.next.next.val == 6
    assert ll.head.next.next.next.next.next.next.next.next == None
    
def testDeleteIndex():
    """test the deleteAtIndex method"""
    lst = [1, 2, 3, 4, 5]
    ll = sll.convert_to_linked_list(lst)
    ll.deleteIndex(0)
    assert ll.size == 4
    assert ll.head.val == 2
    assert ll.head.next.val == 3
    assert ll.head.next.next.val == 4
    assert ll.head.next.next.next.val == 5
    assert ll.head.next.next.next.next == None
    ll.deleteIndex(3)
    assert ll.size == 3
    assert ll.head.val == 2
    assert ll.head.next.val == 3
    assert ll.head.next.next.val == 4
    assert ll.head.next.next.next == None
    ll.deleteIndex(1)
    assert ll.size == 2
    assert ll.head.val == 2
    assert ll.head.next.val == 4
    assert ll.head.next.next == None
    ll.deleteIndex(1)
    assert ll.size == 1
    assert ll.head.val == 2
    assert ll.head.next == None
    ll.deleteIndex(0)
    assert ll.size == 0
    assert ll.head == None
    ll.deleteIndex(0)
    assert ll.size == 0
    assert ll.head == None
    
def testPrintList():
    """test the print method"""
    lst = [1, 2, 3, 4, 5]
    ll = sll.convert_to_linked_list(lst)
    assert ll.printList() == None
    
    
