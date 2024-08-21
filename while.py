class Shape:
    def __init__(self, a):
        self.a = a
        
    def perimeter(self):
        pass

class Circle(Shape):

    def perimeter(self):
        return self.a * 3.14

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2


class Tringle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a * self.b * self.c

cir1 = Circle(2)
print(cir1.perimeter())

rec1 = Rectangle(4, 5)
print(rec1.perimeter())

t1 = Tringle(4,5,6)
print(t1.perimeter())



