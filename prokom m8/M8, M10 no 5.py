def celcius(pil,suhu):
    hasil = 0
    if pil == 1:
        hasil = suhu
    elif pil == 2:
        hasil = (9/5)*suhu+32
    elif pil == 3:
        hasil = suhu+273.15
    elif pil == 4:
        hasil = (4/5)*suhu
    else:
        print("Input salah")
    return hasil

def fahrenheit(pil,suhu):
    hasil = 0
    if pil == 1:
        hasil = (5/9)*(suhu-32)
    elif pil == 2:
        hasil = suhu
    elif pil == 3:
        hasil = (5/9)*(suhu-32)+273.15
    elif pil == 4:
        hasil = (4/9)*(suhu-32)
    else:
        print("Input salah")
    return hasil

def kelvin(pil,suhu):
    hasil = 0
    if pil == 1:
        hasil = suhu - 273.15
    elif pil == 2:
        hasil = ((9/5)*(suhu-273.15)+32)
    elif pil == 3:
        hasil = suhu
    elif pil == 4:
        hasil = ((4/5)*(suhu-273.15))
    else:
        print("Input salah")
    return hasil

def reamur(pil,suhu):
    hasil = 0
    if pil == 1:
        hasil = (5/4)*suhu
    elif pil == 2:
        hasil = (9/4)*suhu+32
    elif pil == 3:
        hasil = (5/4)*suhu+273.15
    elif pil == 4:
        hasil = suhu
    else:
        print("Input salah")
    return hasil

print("Hitungan konversi suhu")
jenis_suhu = ("1. Celcius", "2. Fahrenheit", "3. Kelvin", "4. Reamur")
for x,suhu in enumerate(jenis_suhu, start=1):
    print(suhu)

print("Dari satuan apa?")
pil1 = int(input("Pilihan : "))
pil = int(input("Konversi ke satuan? :"))
suhu = int(input("Masukkan suhu : "))
if pil1 == 1:
    print(celcius(pil,suhu))
elif pil1 == 2:
    print(fahrenheit(pil,suhu))
elif pil1 == 3:
    print(kelvin(pil,suhu))
elif pil1 == 4:
    print(reamur(pil,suhu))
else:
    print("Terjadi Error")