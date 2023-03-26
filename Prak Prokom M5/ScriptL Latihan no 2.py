#program pengulangan angka membentuk segitiga
n = int(input('masukan bilangan : '))
a_awal = 1
for i in range(n):
    for j in range(i+1):
        print(a_awal, end=" ")
        a_awal += 1
    print()
    
#program pengulangan angka membentuk segitiga2 #masih kurang tepat
print('#program untuk soal no 2')
n = int(input('masukan bilangan :'))
a_awal = 1
del_ind = 0
for i in range(0,n): #Loop pertama digunakan untuk mengatur jumlah baris pada pola
    for j in range(i+1): #loop kedua digunakan untuk mengatur jumlah angka pada setiap baris
        if(j<del_ind):
            pass
        else:
            print(a_awal, end=" ")
        a_awal += 1
    for k in range(i+1): #Loop ketiga digunakan untuk mengatur angka yang dicetak pada bagian kanan dari setiap baris.
        b_awal = a_awal-k-2
        if (k == del_ind):
            pass
        else:
            print(b_awal, end=" ")
    del_ind+=1
    print()
