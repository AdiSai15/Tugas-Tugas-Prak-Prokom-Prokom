#lama Studi Masih Ngawur
mahasiswa = {
    41235: {'Nama': 'Adi', 'Angkatan': 2014, 'IPK': 3.56},
    54321: {'Nama': 'Iwan', 'Angkatan': 2015, 'IPK': 2.25},
    12739: {'Nama': 'Hilmy', 'Angkatan': 2016, 'IPK': 3.56},
    23456: {'Nama': 'Arif', 'Angkatan': 2016, 'IPK': 3.00},
    34567: {'Nama': 'Citra', 'Angkatan': 2015, 'IPK': 3.75},
    45678: {'Nama': 'Donita', 'Angkatan': 2014, 'IPK': 2.75},
    56789: {'Nama': 'Rafillia', 'Angkatan': 2014, 'IPK': 3.99},
    45551: {'Nama': 'Fajar', 'Angkatan': 2015, 'IPK': 2.50},
    78901: {'Nama': 'Ami', 'Angkatan': 2014, 'IPK': 3.20},
    89012: {'Nama': 'Ipung', 'Angkatan': 2016, 'IPK': 3.80},
    12345: {'Nama': 'Indra', 'Angkatan': 2015, 'IPK': 2.80},
    17809: {'Nama': 'Allysa', 'Angkatan': 2014, 'IPK': 3.50},
    22334: {'Nama': 'Nadine', 'Angkatan': 2016, 'IPK': 2.90},
    33445: {'Nama': 'Alam', 'Angkatan': 2015, 'IPK': 3.40},
    44556: {'Nama': 'Nabila', 'Angkatan': 2016, 'IPK': 3.95}
}

tahun_sekarang = 2020
for no_mhs, data_mhs in mahasiswa.items(): # Looping untuk mengecek dan menampilkan predikat kelulusan setiap mahasiswa
    nama = data_mhs['Nama']
    angkatan = data_mhs['Angkatan']
    ipk = data_mhs['IPK']
    tahun_masuk = data_mhs['Angkatan']
    lama_studi = tahun_sekarang - tahun_masuk
    
    if lama_studi <= 4 and ipk > 3.50:
        predikat = 'Dengan Pujian'
    elif lama_studi > 4 and ipk > 3.50:
        predikat = 'Sangat Memuaskan'
    elif 2.75 <= ipk < 3.00:
        predikat = 'Sangat Memuaskan'
    else:
        predikat = 'Memuaskan'
    print(f'{"No Mhs":<13}:', no_mhs)
    print(f'{"Nama":<13}:', nama)
    print(f'{"Angkatan":<13}:', angkatan)
    print(f'{"IPK":<13}:', ipk)
    print(f'{"Lama Studi":<13}:', lama_studi, 'Tahun')
    print(f'{"Predikat":<13}:', predikat)
    print('\n')
print()