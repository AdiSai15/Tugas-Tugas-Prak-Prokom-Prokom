def tambah(*args):
    total = 0 
    for x in args:
        total += x
    return total

print(tambah(10,5))
print(tambah(120, 2, 50, 20))
print(tambah(10,50,12))
