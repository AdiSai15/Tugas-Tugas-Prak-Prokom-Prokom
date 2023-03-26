# a gunakan while untuk deret kiri
sebelah_kiri = 7
while True:
    print('5'+'0'*sebelah_kiri)
    sebelah_kiri-=1
    if sebelah_kiri ==-1:
        break

# b gunakan for untuk deret kanan
sebelah_kanan = 7
for sebelah_kanan in range(0,8):
    print('5'+'0'*sebelah_kanan)
    