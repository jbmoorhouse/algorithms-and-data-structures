from .._node import Node

import pytest

# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def valid_node():
    return Node(data=10, left=None, right=None)

@pytest.fixture
def valid_nested_node():
    return Node(data=10, next=Node(data=5, next=None))

# =============================================================================
# Test simple
# =============================================================================

def test_node_constuctor(valid_node):
    attr = {'data': 10, 'left': None, 'right': None}

    assert valid_node.__dict__ == attr

@pytest.mark.parametrize(
    "left, right, new", 
    [(10, None, valid_node), 
     (None, 10, valid_node), 
     (None, valid_node, 10)])
def test_setattr(valid_node, left, right, new):
    msg = f"Bad type for .*, detected .*"

    with pytest.raises(TypeError, match = msg):
         valid_node.left = left
         valid_node.right = right
         valid_node.new = new

def test_repr(valid_node, valid_nested_node):
    assert repr(valid_node) == 'Node(data=10, left=None, right=None)' 
    assert repr(valid_nested_node) == 'Node(data=10, next=Node(data=5, next=None))'