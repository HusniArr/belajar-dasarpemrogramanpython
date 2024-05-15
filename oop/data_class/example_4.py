from dataclasses import dataclass
from typing import Final

FLY : Final = True
CANNOT_FLY : Final = False

@dataclass
class Animal:
    name : str

@dataclass
class Bird(Animal):
    can_fly: bool

    def is_fly(self):
        if(self.can_fly == FLY):
            return "can fly"
        else:
            return "cannot fly"

cow = Animal(name="Cow")
print(cow.name)

chicken = Bird(name="chicken", can_fly=False)
print(chicken.name, chicken.is_fly())