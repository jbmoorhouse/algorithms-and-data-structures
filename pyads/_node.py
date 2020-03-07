"""
"""
# =============================================================================
class Node:   
    """Data structure node which be used in applications such as linked
        list, trees etc.
        
        Parameters
        ----------
        data : int or float
            Simple node contains only numerical data
        pointers : Node or None
            Set an arbritary number of pointers, depending on the data 
            structure type. E.g. Linked list may contain ``next`` and 
            ``prev``. A tree may contain ``left`` and ``right`` etc

        Examples
        --------
        n1 = Node(data = 10)
        n2 = Node(data = 5, left = n1)
        """
         
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

