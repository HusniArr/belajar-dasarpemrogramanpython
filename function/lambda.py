# pengenalan fungsi lambda
def say_hello1():
    print("hello python")

say_hello1()
# output ➜ hello python

say_hello2 = lambda : print("hello python")

say_hello2()
# output ➜ hello python

# Contoh lambda dengan parameter *args:#

def debug1(separator, *params):
    res = []
    for i in range(len(params)):
        res.append(f"param {i}: {params[i]}")
    return separator.join(res)

debug2 = lambda separator, *params : separator.join([f"param {i}: {params[i]}" for i in range(len(params))])

res = debug1(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True)
print(res)
# output ➜ param 0: Darion Mograine, param 1: ['Highlord', 'Horseman of the Ebon Blade', 'Ashbringer'], param 2: True

res = debug2(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True)
print(res)
# output ➜ param 0: Darion Mograine, param 1: ['Highlord', 'Horseman of the Ebon Blade', 'Ashbringer'], param 2: True