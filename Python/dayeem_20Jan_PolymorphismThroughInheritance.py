from math import pi

class Shape:
    def __init__(self, name):
        self.n = name
    
    # abstract class
    def area(self):
        pass
    
    def fact(self):
        return 'Some shape'
    
    def __str__(self):
        return self.n


class Square(Shape):
    def __init__(self, length):
        super().__init__('Square')
        self.l = length
    
    def area(self):
        return self.l ** 2
    
    def fact(self):
        return 'Each angle is 90 degrees'


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.r = radius
    
    def area(self):
        return pi * self.r * self.r


if __name__ == '__main__':
    s = Square(6)
    c = Circle(5)
    print('Square area:', s.area(), '| Fact:', s.fact())
    print('Circle area:', c.area(), '| Fact:', c.fact())
