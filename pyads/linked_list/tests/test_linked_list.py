from .._linked_lists import SinglyLinkedList

import pytest

def test_attr():
    with pytest.raises(AttributeError):
        SinglyLinkedList(1)