from .._linked_lists import (
    SinglyLinkedList
)

import pytest

# =============================================================================
# Fixtures
# =============================================================================

# Singly linked list
@pytest.fixture
def empty_singly():
    return SinglyLinkedList()

@pytest.fixture
def singly_linked_list():
    return SinglyLinkedList(1,2,3,4,5)

# Doubly linked list
@pytest.fixture
def empty_doubly():
    return DoublyLinkedList()

@pytest.fixture
def doubly_linked_list():
    return DoublyLinkedList(1,2,3,4,5)

# Circular linked list
@pytest.fixture
def empty_circular():
    return CircularLinkedList()

@pytest.fixture
def circular_linked_list():
    return CircularLinkedList(1,2,3,4,5)


# =============================================================================
# Mutation
# =============================================================================

def test_append(empty_singly, singly_linked_list):
    # Test append with empty list
    empty_singly.append(1)
    assert repr(empty_singly.head) == "Node(data=1, next=None)"

    empty_singly.append(2)
    assert repr(empty_singly.head) == "Node(data=1, next=Node(data=2, " \
        "next=None))"

    # Test append when instantiated with values
    assert repr(singly_linked_list.head) == "Node(data=1, next=Node(data=2, " \
        "next=Node(data=3, next=Node(data=4, next=Node(data=5, next=None)))))"

    singly_linked_list.append(6)
    assert repr(singly_linked_list.head) == "Node(data=1, next=Node(data=2, " \
        "next=Node(data=3, next=Node(data=4, next=Node(data=5, " \
        "next=Node(data=6, next=None))))))"


def test_append_left(empty_singly, singly_linked_list):
    empty_singly.append_left(1)
    assert repr(empty_singly.head) == "Node(data=1, next=None)"

    singly_linked_list.append_left(6)
    assert repr(singly_linked_list.head) == "Node(data=6, next=Node(data=1, " \
        "next=Node(data=2, next=Node(data=3, next=Node(data=4, next=Node" \
        "(data=5, next=None))))))"


insert = [
    (0, 10, "Node(data=10, next=Node(data=1, next=Node(data=2, " \
     "next=Node(data=3, next=Node(data=4, next=Node(data=5, next=None))))))"), 
    (5, 10, "Node(data=1, next=Node(data=2, next=Node(data=3, " \
     "next=Node(data=4, next=Node(data=5, next=Node(data=10, next=None))))))"),
    (3, 10, "Node(data=1, next=Node(data=2, next=Node(data=3, " \
     "next=Node(data=10, next=Node(data=4, next=Node(data=5, next=None))))))")
]

@pytest.mark.parametrize("position, data, solution", insert)
def test_insert(
    empty_singly, 
    singly_linked_list, 
    position, 
    data, 
    solution):

    singly_linked_list.insert(position, data)
    assert repr(singly_linked_list.head) == solution

def test_pop(empty_singly, singly_linked_list):
    msg = "Object is empty. Cannot remove items"

    with pytest.raises(IndexError, match=msg):
        empty_singly.pop()

    assert singly_linked_list.pop() == 5
    assert repr(singly_linked_list.head) == "Node(data=1, next=Node(data=2, " \
        "next=Node(data=3, next=Node(data=4, next=None))))"
    assert singly_linked_list.length == 4

    assert singly_linked_list.pop() == 4
    assert repr(singly_linked_list.head) == "Node(data=1, next=Node(data=2, " \
        "next=Node(data=3, next=None)))"
    assert singly_linked_list.length == 3

def test_pop_left(empty_singly, singly_linked_list):
    msg = "Object is empty. Cannot remove items"

    with pytest.raises(IndexError, match=msg):
        empty_singly.pop_left()

    assert singly_linked_list.pop_left() == 1
    assert repr(singly_linked_list.head) == "Node(data=2, next=Node(data=3, " \
        "next=Node(data=4, next=Node(data=5, next=None))))"
    assert singly_linked_list.length == 4

    assert singly_linked_list.pop_left() == 2
    assert repr(singly_linked_list.head) == "Node(data=3, next=Node(data=4, " \
        "next=Node(data=5, next=None)))"
    assert singly_linked_list.length == 3


def test_remove(empty_singly, singly_linked_list):
    msg = "``position`` out of range"        

    with pytest.raises(IndexError, match=msg):
        empty_singly.remove(1)
        singly_linked_list.remove(5)
        singly_linked_list.remove(-1)

    singly_linked_list.remove(0)
    assert repr(singly_linked_list.head) == "Node(data=2, next=Node(data=3, " \
        "next=Node(data=4, next=Node(data=5, next=None))))"
    assert singly_linked_list.length == 4
    
    singly_linked_list.remove(3)
    assert repr(singly_linked_list.head) == "Node(data=2, next=Node(data=3, " \
        "next=Node(data=4, next=None)))"
    assert singly_linked_list.length == 3

    singly_linked_list.remove(1)
    assert repr(singly_linked_list.head) == "Node(data=2, next=Node(data=4, " \
        "next=None))"
    assert singly_linked_list.length == 2


def test_reverse(empty_singly, singly_linked_list):
    empty_singly.reverse()
    assert str(empty_singly) == "None"
    assert repr(empty_singly) == 'SinglyLinkedList()'

    singly_linked_list.reverse()
    assert repr(singly_linked_list.head) == "Node(data=5, next=Node(data=4, " \
        "next=Node(data=3, next=Node(data=2, next=Node(data=1, next=None)))))"

    singly_linked_list.reverse()
    assert repr(singly_linked_list.head) == "Node(data=1, next=Node(data=2, " \
        "next=Node(data=3, next=Node(data=4, next=Node(data=5, next=None)))))"


# =============================================================================
# Test __repr__ and __str__
# =============================================================================

def test_str(
    empty_singly, 
    singly_linked_list, 
    empty_doubly, 
    doubly_linked_list, 
    empty_circular, 
    circular_linked_list):

    # Singly linked list
    assert str(empty_singly) == "None"
    assert str(singly_linked_list) == "Node(1) -> Node(2) -> Node(3) -> " \
        "Node(4) -> Node(5) -> None"

    # Doubly linked list
    assert str(empty_doubly) == "None"
    assert str(doubly_linked_list) == "Node(1) <-> Node(2) <-> Node(3) <-> " \
        "Node(4) <-> Node(5) <-> None"

    # Circular linked list
    # assert print(empty_circular) == None
    # assert print(circular_linked_list) == "Node(1) -> Node(2) -> " \
    #     "Node(3) -> Node(4) -> Node(5)"

def test_repr(
    empty_singly, 
    singly_linked_list, 
    empty_doubly, 
    doubly_linked_list, 
    empty_circular, 
    circular_linked_list):

    assert repr(empty_singly) == "SinglyLinkedList()"
    assert repr(singly_linked_list) == "SinglyLinkedList(1, 2, 3, 4, 5)"

    assert repr(empty_doubly) == "DoublyLinkedList()"
    assert repr(doubly_linked_list) == "DoublyLinkedList(1, 2, 3, 4, 5)"

    # assert print(empty_circular) == "SinglyLinkedList()"
    # assert print(circular_linked_list) == "SinglyLinkedList(1, 2, 3, 4, 5)"

