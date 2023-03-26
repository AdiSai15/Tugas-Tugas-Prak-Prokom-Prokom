#potongan skrip progam pola segitiga bintang
#program asli
tinggi = int(input('Masukan bilangan bulat yang akan dibuat pola segitiga bintangnya :'))
baris = 1

print ('Pola segitiga bintangnya adalah:')
while baris <= tinggi:
    kolom = 1
    while kolom <= baris:
        print("*", end = ' ')
        kolom +=1
    print()
    baris +=1
    
#A program modif
tinggi = int(input('Masukan bilangan bulat yang akan dibuat pola segitiga bintangnya :'))
print ('Pola segitiga bintangnya adalah:')
for tinggi in range(1, tinggi+1):
    print('* '*tinggi)
    
#B program modif
tinggi = int(input('Masukan bilangan bulat yang akan dibuat pola segitiga bintangnya :'))
print ('Pola segitiga bintangnya adalah:')
for tinggi in range(tinggi, 0, -1):
    print('* '*tinggi)
    
#B program modif while
tinggi = int(input('Masukkan bilangan bulat yang akan dibuat pola segitiga bintangnya : '))
baris = tinggi
print('Pola segitiga bintangnya adalah : ')
while baris >= 1:
    kolom = 1
    while kolom <= baris:
        print("*", end=' ')
        kolom += 1
    print()
    baris -= 1


