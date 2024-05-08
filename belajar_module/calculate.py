note = "module calculate contains mathematic functions"

def calc_hypotenuse(a, b):
    return sqrt(pow(a) + pow(b))

def pow(n, p=2):
    return n ** p

def sqrt(x):
    n = 1
    for _ in range(10):
        n = (n + x/n) * 0.5
    return n
    
# Module calculate berisi 1 buah variabel dan 3 buah fungsi:

# Variabel note berisi string
# Fungsi calc_hypotenuse() untuk menghitung nilai hipotenusa dari a dan b
# Fungsi pow() untuk meperingkas operasi pangkat
# Fungsi sqrt() untuk mencari akar kuadrat
# Kesemua unit di atas di-import ke my_program untuk kemudian digunakan dalam perhitungan pencarian nilai hipotenusa.