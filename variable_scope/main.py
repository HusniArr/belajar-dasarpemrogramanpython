name = "Cleaver Bmurglbrm" ## variabel global yang dideklarasikan tidak dalam suatu block
print("greetings", name) 

def greet():
    today = "Saturday"  ## variabel local yang dideklarasikan di dalam suatu block
    print("happy", today)

if name:
    greet()
    greet_message = "have a good day"
    print("hello", name, greet_message)


