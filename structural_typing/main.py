from abc import ABC, abstractmethod

class Object2D(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

def do_the_math(obj: Object2D):
    area = obj.calculate_area()
    print(f"area of {type(obj).__name__}: {area}")

class Triangle(Object2D):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calculate_area(self):
        return 1/2 * self.b * self.h
    
class Circle(Object2D):
    def __init__(self, r):
        self.r = r
    def calculate_area(self):
        return 3.14 * self.r * self.r
    
class Square(Object2D):
    def __init__(self, s):
        self.s = s
    def calculate_area(self):
        return self.s * self.s
    
class NotReallyA2dObject:
    @classmethod
    def calculate_area(cls):
        return "where is the number?"

do_the_math(Triangle(3,4))
do_the_math(Circle(4))
do_the_math(Square(5))
do_the_math(NotReallyA2dObject)