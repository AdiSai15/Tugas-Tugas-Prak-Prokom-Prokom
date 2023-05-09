def kelas(h1,h2,d):
    dh= abs(h2-h1)
    tk = dh/d*100
    if 0<=tk<8:
        print("Datar")
    elif 8<=tk<15:
        print("Landai")
    elif 15<=tk<25:
        print("Agak Curam")
    elif 25<=tk<40:
        print("Curam")
    elif tk>=40:
        print("Sangat curam")

h1 = float(input("Masukan tinggi titik 1 : "))
h2 = float(input("Masukan tinggi titik 2 : "))
d = float(input("Masukan jarak antar titik : "))
kelas(h1,h2,d)
