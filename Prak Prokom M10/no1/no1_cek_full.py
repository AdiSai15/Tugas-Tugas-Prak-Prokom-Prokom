from cek_bulan import*
from cek_tahun_kbst import*

if  tahun_kabisat(2060):
    print("Tahun Kabisat")
else:
    print("Tahun Bukan kabisat")
print("Jumlah hari pada Tahun", tahun_kabisat(2060), "bulan", bulan_taun(2), "adalah", jmlh_hari(2060), "hari")