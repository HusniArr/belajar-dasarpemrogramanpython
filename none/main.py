# None merupakan object bawaan Python yang umumnya digunakan untuk merepresentasikan nilai kosong atau null

def inspec_data(data):
    if data == None:
        print("data is empty.")
    else:
        print(f"data: {data}, type: {type(data).__name__}")

data = 0
inspec_data(data)

data = ""
inspec_data(data)

data = None
inspec_data(data)