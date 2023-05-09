print('''Program membuat fungsi hitungan luas dan keliling segitiga siku-siku''')
#definisi fungsi segitiga

def segitiga(a,b):
    global luas, keliling
    sisi_miring = ((a**2)+(b**2))**0.5
    print("Panjang sisi miring segitiga siku-siku =", sisi_miring)
    luas = 0.5*a*b
    keliling = a+b+sisi_miring
    return(luas,keliling)

#program utama
print("Masukan panjang 2 sisi segitiga yang saling tegak lurus")
a = float(input("Panjang sisi a = "))
b = float(input("Panjang sisi b = "))

segitiga(a,b)
print("Luas Segitiga siku-siku = ", luas)
print("Keliling segitiga siku-siku =", keliling)



#SOAL B
print('''Program membuat fungsi hitungan luas dan keliling segitiga siku-siku ''')

# Definisi fungsi segitiga
def segitiga():
    print("Masukan panjang 2 sisi segitiga yang saling tegak lurus")
    a = float(input("Panjang sisi a = "))
    b = float(input("Panjang sisi b = "))

    # variabel luas dan keliling sebagai variabel lokal
    sisi_miring = ((a**2)+(b**2))**0.5
    print("Panjang sisi miring segitiga siku-siku =", sisi_miring)
    luas = 0.5*a*b
    keliling = a+b+sisi_miring
    print("Luas segitiga siku-siku =", luas)
    print("Keliling segitiga siku-siku =", keliling)

# panggil fungsi segitiga
segitiga()

