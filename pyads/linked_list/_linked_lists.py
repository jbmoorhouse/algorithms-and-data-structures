

class LinkedList:
    def __init__(self, **pointers):
        self.head = None
    
    def append(self):
        pass

    def appendleft(self):
        pass
    
    def insert(self):
        pass

    def pop(self):
        pass

    def popleft(self):
        pass

    def remove(self):
        pass

    def reverse(self):
        pass

class SinglyLinkedList(LinkedList):
    def __init__(self, head, pointers):
        super().__init__(head = head, pointers = pointers)
    
class DoublyLinkedList(LinkedList):
    def __init__(self, head, pointers):
        super().__init__(head = head, pointers = pointers)

class CircularLinkedList(LinkedList):
    def __init__(self, head, pointers):
        super().__init__(head = head, pointers = pointers)

class EfficientLinkedList(LinkedList):
    def __init__(self, head, pointers):
        super().__init__(head = head, pointers = pointers)

class SkipLinkedList(LinkedList):
    def __init__(self, head, pointers):
        super().__init__(head = head, pointers = pointers)