makan = ['Nasi Goreng', 'Bakmi Godog', 'Mie Nyemek', 'Bakmi Goreng', 'Kwetiaw']
minum = ['Teh Panas', 'Jeruk Panas', 'Kopi', 'Bajigur']

pesanan_awal = ([makan[0],makan[0],
                makan[1],
                makan[3], makan[3], makan[3],
                minum[0], 
                minum[1], 
                minum[3], minum[3], minum[3]])
print('Pesanan Awal:', tuple(pesanan_awal))
pesanan_awal[9:] = [minum[2]]*3
print('Pesanan Rekap:', tuple(pesanan_awal))
pesanan_akhir = pesanan_awal + ([minum[1]]*2)
print('Pesanan Akhir:', tuple(pesanan_akhir))

pesanan_makanan = {
    'Nasi Goreng': 2,
    'Bakmi Godog': 1, 
    'Mie Nyemek': 0, 
    'Bakmi Goreng': 3, 
    'Kwetiau': 0
    }
pesanan_minuman = {
    'Teh Panas': 2, 
    'Jeruk Panas': 3, 
    'Kopi': 3, 
    'Bajigur': 0
    }
#while
print('Rekap pesanan makanan:')
i = 1
while i <= len(pesanan_makanan):
    for makanan, jumlah in pesanan_makanan.items():
        if i == list(pesanan_makanan.keys()).index(makanan) + 1:
            print(f'{i}. {makanan}\t= {jumlah}')
            i += 1
            break
        
print('\nRekap pesanan minuman:')
i = 1
while i <= len(pesanan_minuman):
    for makanan, jumlah in pesanan_minuman.items():
        if i == list(pesanan_minuman.keys()).index(makanan) + 1:
            print(f'{i}. {makanan}\t= {jumlah}')
            i += 1
            break
#for
print('Rekap pesanan makanan:')
for i, (makanan, jumlah) in enumerate(pesanan_makanan.items(), start=1):
    print(f"{i}. {makanan:<15}= {jumlah}")
print('\nRekap pesanan minuman:')
for i, (minuman, jumlah) in enumerate(pesanan_minuman.items(), start=1):
    print(f"{i}. {minuman:<15}= {jumlah}")
