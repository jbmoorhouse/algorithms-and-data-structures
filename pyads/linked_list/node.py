"""
"""
# =============================================================================
class Node:
    def __init__(self, data, **pointers):
        self.data = data
            
    def __setattr__(self, name, value):
        if name == 'data' and isinstance(value, int):
            pass
        elif not (isinstance(value, Node) or value is None):
            raise TypeError(f"Bad type for {name}, detected {type(value)}")
        
        self.__dict__[name] = value

