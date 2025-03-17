class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def __getattribute__(self, item):
        
        return object.__getattribute__(self, item)
    
    def __getattr__(self, item):
        return 'This attribute is not available'
    
c = Car("Toyota", "Corolla")
print(c.make)    
print(c.color)     
