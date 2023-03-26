#program skema menampilkan pola segitiga pascal
bil = int(input('masukan bilangan :'))
for n in range (1, bil+2):
    bil1 = 1
    for k  in range(1, n+1):
        print(bil1, end=' ')
        bil1 = bil1*(n-k)//k
    print()
    


#modifikasi
bil = int(input('masukan bilangan :'))
for bil in range (1, bil+2):
    bil1 = 1
    for bil1  in range(1, bil+1):
        print(bil1, end=' ')
        bil1 = bil1*(bil-bil1)//bil1
    print()