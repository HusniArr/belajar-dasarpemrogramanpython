# deklarasi data list berisi element tuple
data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
]

# append tuple ke list
data.append(("noob", 6, False, ["brotherhood of shadow"]))

# append tuple ke list
data.append(("tifa lockart", 2, True, ['avalanche']))

# print data
print("name | rank | win | affliation")
print("------------------------------")
for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()