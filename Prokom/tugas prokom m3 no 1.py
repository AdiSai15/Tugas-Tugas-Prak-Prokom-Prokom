'Skrip program penggunaan variabel dan penugasannya'
'serta mengatur tampilannya, disimpan dengan nama file'
'prak3_variabel.py'

#operator penugasan
x, y, z = 100, 25.45, -28
x /= 5 #identik dengan x = x/5
y //= 3 #identik dengan y = y//3
z %= -5 #identik dengan z = z%-5

#penulisan bilangan riil
bil1 = 75.123456789012345
bil2 = int(75.123456789012345) #konversi ke tipe integer
bil3 = str(75.123456789012345) #konversi ke tipe string
bil4 = "{:e}".format(bil1) #konversi ke format scientific
bil5 = "{:.7f}".format(bil1) #tapilkan 7 angka desimal
bil6 = "{:.3f}".format(-bil1) #tampilkan -75.123
bil7 = "{:3E}".format(bil1) #tampilkan 7.512E+03
bil8 = "{:3e}".format(bil1) #tampilkan 7.512e-2
bil9 = "{:,}".format(75.123456789012345) #tampilkan 751,234,567.8901
bil10 = "{:.2f}%".format(75.123456789012345) #tampilkan 75.12%
#konversi nilai integer bil1 ke tipe biner tanpa awalan "0b"
bil = "{:b}".format(bil2)
#konversi nilai integer bil1 ke tipe biner dengan awalan "0b"
bil02 = "{:d}".format(bil2)
