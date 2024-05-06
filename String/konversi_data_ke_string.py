number = 24
string1 = f"{number}"
print(string1) #output -> 24

item = [1, 2, 3, 4]
string2 = f"{item}" #output -> [1, 2, 3, 4]

obj = {
    "name": "AMD Rayzen 5600g",
    "type": "processor",
    "igpu": True
}

string3 = f"{obj}"
print(string3) # output {'name':'AMD Rayzen 5600g', 'type': 'processor', 'igpu': True}
