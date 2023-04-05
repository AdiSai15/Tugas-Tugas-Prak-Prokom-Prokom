menu_makan = {
            'Nasi Goreng': 20000,
            'Bakmi Godog': 25000,
            'Mie Nyemek': 17500,
            'Bakmi Goreng': 28000,
            'Kwetiaw': 22500
            }
menu_minum = {
            'Teh Panas': 3000,
            'Jeruk Panas': 4500,
            'Kopi': 8000,
            'Bajigur':10000
            }
makan = ['Nasi Goreng', 'Bakmi Godog', 'Mie Nyemek', 'Bakmi Goreng', 'Kwetiaw']
minum = ['Teh Panas', 'Jeruk Panas', 'Kopi', 'Bajigur']

pesanan_awal = ([makan[0],makan[0],
                makan[1],
                makan[3], makan[3], makan[3],
                minum[0], 
                minum[1], 
                minum[3], minum[3], minum[3]])
pesanan_awal[9:] = [minum[2]]*3
print('Pesanan Awal:',pesanan_awal)
pesanan_akhir = pesanan_awal + ([minum[1]]*2)
print('Pesanan Akhir:', pesanan_akhir)

all_menu = tuple(makan+minum)
all_price = dict(menu_makan | menu_minum)
count=0
total = 0
l = f'{"Makanan/Minuman":<15}{"qty":>4}{"Harga":>7}{"Total":>8}'
print(f'{"Nota Pembayaran":^33}')
print('='*len(l))
print(l,'\n','-'*len(l))
#print(f'{all_menu[i]:<15}{count:>3}{all_price[all_menu[i]]:>7}{all_price[all_menu[i]]*count:>8}')
for i in range(len(all_menu)):
    for j in pesanan_akhir:
        if j == all_menu[i]:
            count+=1
    if count != 0:
        total += all_price[all_menu[i]]*count
        print(f'{all_menu[i]:<15}{count:>4}{all_price[all_menu[i]]:>7}{all_price[all_menu[i]]*count:>8}')
    count=0
print('-'*len(l))
print(f'{"JUMLAH":>26}{total:>8}')
print('='*len(l))