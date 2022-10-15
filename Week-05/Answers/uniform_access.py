# بسم الله الرحمن الرحيم

class Student:
    def __init__(self, f_name, l_name, *args, **kwargs):
        self.f_name = f_name
        self.l_name = l_name

    @property
    def full_name(self):
        return f'{self.f_name} {self.l_name}'

b = Student('Bahy', 'Ahmed')
# print(b.f_name)
print(b.full_name)

    