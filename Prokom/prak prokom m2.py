#no 3
artis = "isyana sarasvati"
lagu = "keep being you"
rilis = 2014
copy = 1500000
album = "explore!"
print('Lagu {} yang dinyanyikan "{}" dari album {} yang dirilis pada tahun {} telah terjual sebanyak {} kopi '.format("keep being you".replace("keep being you", '"keep being you"').title(), artis.title(), "explore!".replace("explore!", '"explore!"').title(), rilis, "1500000".replace("1500000", "15.000.000")))

#no 2 c masih revisi
print('Lagu {lagu} yang dinyanyikan "{artis}" dari album {explore} yang dirilis pada tahun {tahun} telah terjual sebanyak {jumlah} kopi'.format(lagu='"keep being you"'.title(), artis="isyana sarasvati".title(), explore='"explore!"'.title(), tahun=2014, jumlah='1500000'.replace('1500000','15.000.000')))
print('Lagu {lagu} yang dinyanyikan "{artis}" dari album {album} yang dirilis pada tahun {rilis} telah terjual sebanyak {copy} kopi'.format(lagu='"keep being you"'.title(), artis="isyana sarasvati".title(), album='"explore!"'.title(), rilis=2014, copy='{:,}'.format(copy*10)))
