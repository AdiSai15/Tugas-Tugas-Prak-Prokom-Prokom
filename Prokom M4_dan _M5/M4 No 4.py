#modifikasi program no 3 untuk menampilkan tahun kabisat dari 1900-2200
for Tahun in range(1900,2200):
    if Tahun % 400 == 0:
        print(Tahun,end=' ')
    elif Tahun % 4 == 0 and Tahun % 100!=0:
        print(Tahun,end=' ') 
    