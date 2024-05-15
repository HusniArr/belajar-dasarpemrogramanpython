# intance method
def do_the_math(obj):
    area = obj.calculate_area()
    print(f"area of {type(obj).__name__}: {area}")

class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    
    def calculate_area(self):
        return 1/2 * self.b * self.h
    
# attribut berisi closure

def number_10():
    return 10

class AreaOf2X10:
    def __init__(self) -> None:
        self.calculate_area = number_10

# attribute berisi lambda

import random

class AreaOfRandomInt:
    def __init__(self) -> None:
        self.calculate_area = lambda : random.randint(0, 10) * 2

# class method
class NotReallyA2dObject:
    @classmethod
    def calculate_area(cls):
        return "Where is the number?"
    
obj1 = Triangle(5, 30)
do_the_math(obj1)

obj2 = AreaOf2X10()
do_the_math(obj2)

obj3 = AreaOfRandomInt()
do_the_math(obj3)

do_the_math(NotReallyA2dObject)


