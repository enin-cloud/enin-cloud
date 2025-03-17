class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)



    def __setattr__(self, key, value):
        print(key, value)
        if   key == 'name' and value == '' :
            raise ValueError('Name cannot be empty!')
        elif key == 'age' and value < 0:
            raise ValueError("Age must be a positive number!")
        else:
            return object.__setattr__(self, key, value)
p = Person("John", 25)  
p.name = "Alice"     
p.age = 30              
p.name = ""           
p.age = -5
