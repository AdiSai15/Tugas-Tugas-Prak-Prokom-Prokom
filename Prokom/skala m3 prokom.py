kcp_rata = 60 #km/jam
jp = 8 #cm
skala = 1/1500000 #per cm
waktu1 = 07.30 #jam

#rumus 
js=(jp/skala)/100000
waktu = (js/kcp_rata)
waktu_tiba = waktu1+waktu
#hasil
print('Jarak Sebenarnya',js,'Km')
print(waktu, 'jam')
print('Waktu tiba pukul', "{:.2f}".format(waktu_tiba))