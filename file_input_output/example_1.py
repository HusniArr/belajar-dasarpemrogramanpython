# keyword with #
with open("file.txt", "w", encoding="utf-8") as f:
    print("file is closed:", f.closed)

print("file is closed:", f.closed)


# menulis file #
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("hello python\n")
    f.write("how are you?\n")

# append atau menambahkan konten ke file
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("hello coders.\n")

# membaca file
with open("file.txt", "r", encoding="utf-8") as f:
    print(f"line 1: {f.readline()}")
    print(f"line 2: {f.readline()}")
    print(f"line 3: {f.readline()}")
    print(f"line 4: {f.readline()}")
    print(f"line 5: {f.readline()}")

# membaca dan menulis dalam 1 sesi
with open("file.txt", "r+", encoding="utf-8") as f:
    print(f"read:\n{f.read()}")
    f.write("lorem dolar ipsum\n")
    print(f"read:\n{f.read()}")

with open("file.txt", "r+", encoding="utf-8") as f:
    print(f"read:\n{f.read()}")

# mengosongkan isi file
with open("file.txt", "w", encoding="utf-8") as f:
    pass

with open("file.txt", "w", encoding="utf-8"):
    pass

open("file.txt", "w", encoding="utf-8").close()

# menghapus file atau folder
import os
os.remove("C:\\laragon\\www\\belajar-dasarpemrogramanpython\\file_input_output\\file.txt")

os.rmdir("C:\\laragon\\www\\belajar-dasarpemrogramanpython\\file_input_output")