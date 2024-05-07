#pengelan *args
def sum_then_print(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    print(total)

sum_then_print(2, 3, 4, 5, 4)
# output ➜ 18

# kombinasi positional argument dan *args
def sum_then_print(message, *numbers, suffix_message):
    total = 0
    for n in numbers:
        total = total + n
    print(f"{message} {total} {suffix_message}")

sum_then_print("total nilai:", 2, 3, 4, 5, 4, suffix_message="selesai!")
# output ➜ total nilai: 18 selesai!