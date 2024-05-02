seq = []
for i in range(1, 10):
    if i % 2 == 0:
        seq.append(i * 2)
    else:
        seq.append(i * 3)
print(seq)

# atau bisa diringkas lagi kodenya
seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1,10)]
print(seq)