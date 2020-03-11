from .._node import Node

from abc import ABCMeta, abstractmethod

# =============================================================================
# Base linked list
# =============================================================================

class LinkedList(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *values):
        self.head = None
        
        for v in values:
            self.append(v)
        
    def __iter__(self):
        self.curr = self.head
        return self
    
    def __next__(self):
        curr = self.curr
        
        while curr:
            temp, self.curr = curr, curr.next
            return temp.data
            
        raise StopIteration
    
    def _format_str(self, has_tail=True):
        values = [f"Node({v})" for v in self]
        
        return values + ["None"] if has_tail else values 

    def _check_length(self):
        if not self.head:
            raise IndexError(
        "``pop`` may not be use with an emtpy linked list") 
    
    def append(self, data):
        if not self.head:
            self.head = Node(data = data, next=None)
        else:
            curr = self.head
            
            while curr.next:
                curr = curr.next
                
            curr.next = Node(data=data, next=None)

    def append_left(self, data):
        self.head = Node(data=data, next=self.head) 
    
    def insert(self, position, data):
        if position == 0:
            self.append_left(data=data)
        else:
            pos, curr = 0, self.head

            while pos < position - 1:
                curr = curr.next
                pos += 1

            temp = curr.next
            curr.next = Node(data=data, next=temp)

    def pop(self):
        self._check_length()

        curr, prev = self.head, None
        while curr.next:
            prev, curr = curr, curr.next
            
        if prev:
            prev.next = None
        else:
            self.head = None
            
        return curr.data
    

    def pop_left(self):
        self._check_length()

        curr = self.head
        self.head = curr.next

        return curr.data

    def remove(self):
        pass

    def reverse(self):
        pass

# =============================================================================
# Public Objects
# =============================================================================

class SinglyLinkedList(LinkedList):
    def __init__(self, *values):
        super().__init__(*values)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(str(v) for v in self)})"

    def __str__(self):
        return " -> ".join(self._format_str())
            
            
class DoublyLinkedList(LinkedList):
    def __init__(self, *values):
        super().__init__(*values)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(str(v) for v in self)})"

    def __str__(self):
        return " <-> ".join(self._format_str())

class CircularLinkedList(SinglyLinkedList):
    def __init__(self, *values):
        super().__init__(*values)

