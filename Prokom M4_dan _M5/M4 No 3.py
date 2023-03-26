#program if else pada tahun

Tahun = int(input('Input Tahun : '))
if Tahun % 400 == 0:
    print(Tahun, 'Tahun Kabisat')
elif Tahun % 4 == 0 and Tahun % 100!=0:
    print(Tahun, 'Tahun Kabisat')
else:
    print(Tahun, 'Bukan Tahun Kabisat')