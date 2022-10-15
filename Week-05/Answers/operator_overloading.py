# بسم الله الرحمن الرحيم

# Overloading

# int add(int a, int b){ return a + b; }
# float x; x = add(1.2, 4.6);
# float add(float a, float b) { return a + b; }

# Operator Overloading

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, point_b):
        return Point(self.a + point_b.a, self.b + point_b.b)

    def __repr__(self):
        return f'Point: x = {self.a}, y = {self.b}'

def main():
    a = Point(1,2)
    print(a)
    b = Point(3,4)
    print(b)
    c = a + b
    print(c)

if __name__ == '__main__':
    main()