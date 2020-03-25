
# =============================================================================
# Base node
# =============================================================================

class Node:   
    """Non-public API.
    
    Base node class to be used when constructing specialist nodes for simple 
    data structures, such as linked lists, trees etc.
    """
         
    def __init__(self, data, **pointers):
        self.data = data
        
        for k, v in pointers.items():
            setattr(self, k, v)
            
    def __repr__(self):
        attr = ", ".join(
            f"{attr}={value!r}" for attr, value in self.__dict__.items())

        return f"{self.__class__.__name__}({attr})"

    def __str__(self):
        return f"{self.__class__.__name__}({self.data})"
                
    def __setattr__(self, name, value):
        err_msg = f"Bad type for `{name}`, detected {type(value)}."
        
        if name == 'data':
            if not isinstance(value, (int, float)):
                raise TypeError(
                f"{err_msg} Should be <class 'int'> or <class 'float'>")
        elif not (isinstance(value, type(self)) or value is None):
            raise TypeError(f"{err_msg} Should be {type(self)}")
            
        super().__setattr__(name, value)


# =============================================================================
# Public API
# =============================================================================

class SinglyNode(Node):
    """Singly linked list Node for numerical data

    Definition of a singly linked list node. This class should not be used in
    isolation to construct or mutate a singly linked list. Instead, a seperate
    class should be defined to create these behaviours. i.e a linked list is 
    defined as a composite data structure, which contains N SinglyNodes.
    
    Parameters
    ----------
    data : int or float
        Numerical data to be stored in the node
    next : SinglyNode, default None
        Pointer to the next element in the linked list objezt
    
    Examples
    --------
    # Only a single node

    >>> sn = SinglyNode(data=1)
    ...
    >>> print(sn)
    ... SinglyNode(1)
    ...
    >>> repr(sn)
    ... 'SinglyNode(data=1, next=None)'

    # The following behaviour is not advised.

    >>> sn = SinglyNode(data=1, next=SinglyNode(data=2))
    ...
    >>> print(sn)
    ... SinglyNode(1) 
    ...
    >>> repr(sn)
    ... 'SinglyNode(data=1, next=SinglyNode(data=2, next=None))'

    # Bad inputs 

    >>> sn = SinglyNode(data=1, next=2)
    ... TypeError: Bad type for `next`, detected <class 'int'>. Should be 
        <class '__main__.SinglyNode'>

    >>> sn = SinglyNode(data="a") 
    ... TypeError: Bad type for `data`, detected <class 'str'>. Should be 
        <class 'int'> or <class 'float'>
    """
    
    def __init__(self, data, next=None):
        super().__init__(data = data, next=next)
    

class DoublyNode(Node):
    def __init__(self, data, next=None, prev=None):
        super().__init__(data = data, next=next, prev=prev)
        

