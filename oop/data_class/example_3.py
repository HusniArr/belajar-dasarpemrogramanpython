# frozen attribute
# Frozen data class adalah data class yang immutable, artinya setelah dideklarasikan maka tidak bisa diubah nilai attribute-nya.

from dataclasses import dataclass

@dataclass(frozen=True)
class Fruit:
    name : str
    flavor : tuple

apple = Fruit("apple", ("sweet", "tart"))
apple.name = "red apple"

print(apple.name)

# output error #
# Traceback (most recent call last):
#   File "c:\laragon\www\belajar-dasarpemrogramanpython\oop\data_class\example_3.py", line 9, in <module>
#     apple.name = "red apple"
#   File "<string>", line 4, in __setattr__
# dataclasses.FrozenInstanceError: cannot assign to field 'name'
