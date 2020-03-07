"""
"""
# =============================================================================
class Node:    
    def __init__(self, data, **pointers):
        self.data = data
        
        for k, v in pointers.items():
            setattr(self, k, v)
            
    def __repr__(self):
        attr = ", ".join(
            f"{attr}={value!r}" for attr, value in self.__dict__.items())
            
        return f"{self.__class__.__name__}({attr})"
                
    def __setattr__(self, name, value):
        if name == 'data':
            pass
        elif not (isinstance(value, Node) or value is None):
            raise TypeError(f"Bad type for {name}, detected {type(value)}")
    
        self.__dict__[name] = value

