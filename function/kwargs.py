def print_data(**data):
    print(f"type: {type(data)}")
    print(f"data: {data}")

    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data(phone="nokia 3310", discontinue=False, year=2000, networks=["GSM", "TDMA"])
# output ↓
#
# type: <class 'dict'>
# data: {'phone': 'nokia 3310', 'discontinue': False, 'year': 2000, 'networks': ['GSM', 'TDMA']}
# 
# param: phone, value: nokia 3310
# param: discontinue, value: False
# param: year, value: 2000
# param: networks, value: ['GSM', 'TDMA']

# kombinasi positional argument, args, keyword argument dan kwargs#
def print_all(message, *params, say_something, **others):
    print(f"message: {message}")
    print(f"params: {params}")
    print(f"say_something: {say_something}")
    print(f"others: {others}")

print_all("hello world", 1, True, ("yesn't", "nope"), say_something="how are you", name="nokia 3310", discontinued=True, year_released=2000)
# output ↓
#
# message: hello world
# params: (1, True, ("yesn't", 'nope'))
# say_something: how are you
# others: {'name': 'nokia 3310', 'discontinued': True, 'year_released': 2000}