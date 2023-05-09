def hitung_rata(list_angka):
    jumlah = 0
    for angka in list_angka:
        jumlah += angka
    rata = jumlah / len(list_angka)
    return jumlah, rata

def ubah_list(list_awal, indeks, nilai_baru):
    list_awal[indeks] = nilai_baru
    return list_awal

list_awal = [20, -15, 10, 5, 25, 40, -15, -5, 5, 20]
print("Isi list sebelum dilakukan perubahan adalah:", list_awal)

jumlah_awal, rata_awal = hitung_rata(list_awal)
print("Hasil penjumlahan semua elemennya :", jumlah_awal, "Nilai rata-ratanya :", rata_awal)

list_ubah = ubah_list(list_awal, 1, 100)
list_ubah = ubah_list(list_ubah, 4, -600)
list_ubah = ubah_list(list_ubah, 7, 1000)

print("Isi list setelah dilakukan perubahan adalah:", list_ubah)
jumlah_ubah, rata_ubah = hitung_rata(list_ubah)
print("Hasil penjumlahan semua elemennya :", jumlah_ubah, "Nilai rata-ratanya :", rata_ubah)
