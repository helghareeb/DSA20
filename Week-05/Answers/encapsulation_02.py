# بسم الله الرحمن الرحيم

class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        assert type(name) == type('abc')
        self.__name = name

    name = property(get_name, set_name)

b = Student('Bahy')
print(b.name)
# b.name = 'Ahmed'
b.name = -500
print(b.name)