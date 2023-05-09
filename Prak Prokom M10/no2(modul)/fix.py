from modul1 import*
from modul2 import*

# Input bilangan
x = int(input("Masukkan bilangan pertama: "))
z = int(input("Masukkan bilangan kedua: "))
y = int(input("Masukkan bilangan ketiga: "))

# Output hasil
print("FPB dari", x, y, "dan", z, "adalah",hitung_fpb(x, y, z))
print("KPK dari", x, y, "dan", z, "adalah",hitung_kpk(x, y, z))