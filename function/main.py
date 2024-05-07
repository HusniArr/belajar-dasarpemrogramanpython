def create_sorcerer(name, age, race, era):
    return {
        "name": name,
        "age": age,
        "race": race,
        "era": era
    }

# positional argument #
obj1 = create_sorcerer("Sukuna", 1000, "incarnation", "heian")
print(obj1)
# output ➜ {'name': 'Sukuna', 'age': 1000, 'race': 'incarnation', 'era': 'heian'}

obj2 = create_sorcerer("Kenjaku", 1000, "human", "1000+ year ago")
print(obj2)
# output ➜ {'name': 'Kenjaku', 'age': 1000, 'race': 'human', 'era': '1000+ year ago'}

obj3 = create_sorcerer("Hajime Kashimo", 400, "human", "400 year ago")
print(obj3)
# output ➜ {'name': 'Hajime Kashimo', 'age': 400, 'race': 'human', 'era': '400 year ago'}

# keyword argument #
obj4 = create_sorcerer(name="Kenjaku", age=1000, race="human", era="1000+ year ago")
print(obj4)
# output ➜ {'name': 'Kenjaku', 'age': 1000, 'race': 'human', 'era': '1000+ year ago'}

obj5 = create_sorcerer("Hajime Kashimo", 400, race="human", era="400 year ago")
print(obj5)
# output ➜ {'name': 'Hajime Kashimo', 'age': 400, 'race': 'human', 'era': '400 year ago'}

# Optional argument
def print_matrix(matrix=[]):
    if len(matrix) == 0:
        print("[]")

    for el in matrix:
        print(el)

print("test print matrix 1:")
print_matrix()

print("test print matrix 2:")
print_matrix([
    [1, 2],
    [5, 6],
])

print("test print matrix 3:")
print_matrix(matrix=[
    [2, 3, 4],
    [3, 1, 6],
])

# kombinasi positional argument, keyword argument, optional argument
def matrix_multiply_scalar(matrix, scalar = 1):
    res = []
    for row in matrix:
        res.append([cell * scalar for cell in row])

    return res

def print_matrix(matrix = []):
    if len(matrix) == 0:
        print("[]")

    for el in matrix:
        print(el)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(f"matrix * scalar {1}:")
res1 = matrix_multiply_scalar(matrix)
print_matrix(res1)
# output ↓
#
# matrix * scalar 1:
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]

print(f"matrix * scalar {3}:")
res2 = matrix_multiply_scalar(matrix, 3)
print_matrix(res2)
# output ↓
#
# matrix * scalar 3:
# [3, 6, 9, 12]
# [15, 18, 21, 24]
# [27, 30, 33, 36]

print(f"matrix * scalar {2}:")
res3 = matrix_multiply_scalar(matrix, scalar=2)
print_matrix(res3)
# output ↓
#
# matrix * scalar 2:
# [2, 4, 6, 8]
# [10, 12, 14, 16]
# [18, 20, 22, 24]

print(f"matrix * scalar {4}:")
res4 = matrix_multiply_scalar(matrix=matrix, scalar=4)
print_matrix(res4)
# output ↓
#
# matrix * scalar 4:
# [2, 4, 6, 8]
# [10, 12, 14, 16]
# [18, 20, 22, 24]

print(f"matrix * scalar {7}:")
res5 = matrix_multiply_scalar(scalar=7, matrix=matrix)
# output ↓
#
# print_matrix(res5)
# matrix * scalar 7:
# [2, 4, 6, 8]
# [10, 12, 14, 16]
# [18, 20, 22, 24]