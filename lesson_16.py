class Rectangle:
    def __init__(self, width, height):
        self.__dict__["width"] = int(width)
        self.__dict__["height"] = int(height)
    
    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError(f"Local attributes are not allowed")
        self.__dict__[key] = value 

r = Rectangle(10, 20)
r.width = 15 
r.height = 25 
r.color = 'red' 
