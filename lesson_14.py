class Counter:
    
    def __getattribute__(self, item):
        print(f'Доступ к атрибуту {item}')
        return object.__getattribute__(self, item)
    
    def __getattr__(self, item):
        return None
    
    c = Counter()
c.value = 5         
print(c.value)      
print(c.name)       
