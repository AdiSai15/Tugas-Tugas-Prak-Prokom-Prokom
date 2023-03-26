#program menampilkan bilangan ganjil dari 1 juka sampai 5 juta urutan turun
for ganjil in range(4999999,1000000, -2):
    print(ganjil, end = ' ')
#program menampilkan bilangan dari 1000 sampai 2000 urutan turun
for genap in range(2000,1000, -2):
    print(genap, end=' ')
#program menampilkan bilangan dari 1000 sampai 2000 urutan turun
for ganjil in range(2000,1000, -1):
    if ganjil %2 !=0:
        print(ganjil, end = ' ')
        
        