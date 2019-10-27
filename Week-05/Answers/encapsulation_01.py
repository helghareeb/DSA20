# بسم الله الرحمن الرحيم

# بسم الله الرحمن الرحيم

class Student:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        assert type(name) == type('abc')
        self.__name = name

b = Student('Bahy')
print(b.name)
# b.name = 'Ahmed'
b.name = -500
print(b.name)