from .._node import Node

class LinkedList:
    def __init__(self, *values):
        self.head = None
        
        for v in values:
            self.append(v)
            
    def _get_values(self):
        curr = self.head
        
        while curr:
            yield str(curr.data)
            curr = curr.next
    
    def _format_str(self, has_tail=True):
        values = [f"Node({v})" for v in self._get_values()]
        
        return values + ["None"] if has_tail else values 
    
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
        pass

    def popleft(self):
        pass

    def remove(self):
        pass

    def reverse(self):
        pass


class SinglyLinkedList(LinkedList):
    def __init__(self, *values):
        super().__init__(*values)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(self._get_values())})"

    def __str__(self):
        return " -> ".join(self._format_str())
            
            
class DoublyLinkedList(LinkedList):
    def __init__(self, *values):
        super().__init__(*values)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(self._get_values())})"

    def __str__(self):
        return " <-> ".join(self._format_str())

class CircularLinkedList(SinglyLinkedList):
    def __init__(self, *values):
        super().__init__(*values)

