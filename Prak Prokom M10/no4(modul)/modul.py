import math
# Modul untuk menghitung luas dari bangun datar
def luas_persegi(s):
    return s*s

def luas_lingkaran(r):
    return math.pi*r*r

def luas_persegi_panjang(p, l):
    return p*l

def luas_trapesium(a1, a2, t):
    return (a1+a2)*t/2

def luas_jajargenjang(a, t):
    return a*t


# Modul untuk menghitung keliling dari bangun datar
def keliling_persegi(s):
    return 4*s

def keliling_lingkaran():
    return 2*math.pi*r

def keliling_persegi_panjang(p, l):
    return 2*(p+l)

def keliling_trapesium(s1, s2, s3, s4):
    return s1+s2+s3+s4

def keliling_jajargenjang(a, sm):
    return 2*(a+sm)


# Program utama
print("Program Menghitung Luas dan Keliling Bangun Datar")
print("Pilih bangun datar yang akan dihitung:")
jns_bgn = ("1. Persegi", "2. Lingkaran", "3. Persegi Panjang", "4. Trapesium", "5. Jajar Genjang")
for x,pilihan in enumerate(jns_bgn, start=1):
    print(pilihan)
    
pilihan = int(input("Masukkan pilihan Anda (1-5): "))

if pilihan == 1: #Persegi
    s = float(input("Masukkan panjang sisi persegi: "))
    print("Luas persegi =", luas_persegi(s))
    print("Keliling persegi =", keliling_persegi(s))
    
elif pilihan == 2: #Lingkaran
    r = float(input("Masukkan jari-jari lingkaran: "))
    print("Luas lingkaran =", luas_lingkaran(r))
    print("Keliling lingkaran =", keliling_lingkaran(r))
    
elif pilihan == 3: #Persegi Panjang
    p = float(input("Masukkan panjang persegi panjang: "))
    l = float(input("Masukkan lebar persegi panjang: "))
    print("Luas persegi panjang =", luas_persegi_panjang(p, l))
    print("Keliling persegi panjang =", keliling_persegi_panjang(p, l))
    
elif pilihan == 4: #Trapesium
    a1 = float(input("Masukkan panjang alas 1 trapesium: "))
    a2 = float(input("Masukkan panjang alas 2 trapesium: "))
    t = float(input("Masukkan tinggi trapesium: "))
    s1 = float(input("Masukkan panjang sisi 1 trapesium: "))
    s2 = float(input("Masukkan panjang sisi 2 trapesium: "))
    s3 = float(input("Masukkan panjang sisi 3 trapesium: "))
    s4 = float(input("Masukkan panjang sisi 4 trapesium: "))
    print("Luas Trapesium = ", luas_trapesium(a1, a2, t))
    print("Keliling Trapesium = ", keliling_trapesium(s1, s2, s3, s4))
    
elif pilihan == 5: #Jajargenjang
    a = float(input("Masukkan panjang alas 1 trapesium: "))
    sm = float(input("Masukkan panjang sisi 2 trapesium: "))
    t = float(input("Masukkan tinggi trapesium: "))
    print("Luas Jajargenjang = ", luas_jajargenjang(a, t))
    print("Keliling Jajargenjang = ", keliling_jajargenjang(a, sm))



#DAH KELAR