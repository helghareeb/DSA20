# بسم الله الرحمن الرحيم

class Student:
    def __init__(self, name, age, dept):
        self.__name = name
        self._age = age
        self.dept = dept

    def get_name(self):
        return self.__name

    def set_name(self, name):
        assert type(name) == type('abc')
        self.__name = name

b = Student('Bahy', 25, 'Pathology')
print(b.get_name())
b.set_name('Ahmed')
print(b.get_name())
# print(b.__name)
# print(b._age)
# print(b.dept)