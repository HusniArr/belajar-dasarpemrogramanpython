str_input = input("Enter your grade: ")
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed exam")
else:
    print("failed")