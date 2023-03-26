#uji program no 6 udah kelar
#A Modifikasi Program
bil = int(input('Masukkan bilangan bulat: '))
jumlah = 0

for x in range(1, bil+1):
    if bil % x == 0:
        jumlah += 1

if jumlah == 2:
    if bil % 2 == 0:
        print('Bilangan yang anda masukkan:', bil, 'merupakan bilangan genap sekaligus bilangan prima')
    else:
        print('Bilangan yang anda masukkan:', bil, 'merupakan bilangan ganjil sekaligus bilangan prima')
else:
    if bil % 2 == 0:
        print('Bilangan yang anda masukkan:', bil, 'merupakan bilangan genap tetapi bukan bilangan prima')
    else:
        print('Bilangan yang anda masukkan:', bil, 'merupakan bilangan ganjil tetapi bukan bilangan prima')

#B Modifikasi Program (masih bingung)
hitung = 0
prima = []

for num in range(2, 101):
    is_prima = True
    for i in range(2, num):
        if num % i == 0:
            is_prima = False
            break
    if is_prima:
        prima.append(num)
        hitung += 1

print('Bilangan prima dari 0 sampai 100 adalah:')
print(*prima, sep=' ')
print('Banyaknya bilangan prima tersebut ada', hitung)