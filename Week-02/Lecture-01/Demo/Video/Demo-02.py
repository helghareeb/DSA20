# In the name of ALLAH

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, op):
        self._x += op._x
        self._y += op._y

    def __lt__(self, op):
        return self._x < op._x and self._y < op._y

    def __eq__(self, op):
        return self._x == op._x and self._y == op._y

    def __le__(self, op):
        return self < op or self == op

    def __repr__(self):
        return f'X = {self._x}, Y = {self._y}'
