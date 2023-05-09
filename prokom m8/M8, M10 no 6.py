def Celcius(C):
    C = float(input("Masukkan besar suhu dalam celcius: "))
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    print("Fahrenheit\t:", str(float((9/5)*C+32))+"° Fahrenheit")
    print("Kelvin\t\t:", str(float(C+273.15))+"° Kelvin")
    print("Reamur\t\t:", str(float((4/5)*C))+"° Reamur")
    return C
def Fahrenheit(F):
    F = float(input("Masukkan besar suhu dalam fahrenheit: "))
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    print("Celcius\t\t:", str(float((5/9)*(F-32)))+"° Celcius")
    print("Kelvin\t\t:", str(float((5/9)*(F-32)+273.15))+"° Kelvin")
    print("Reamur\t\t:", str(float((4/9)*(F-32)))+"° Reamur")
    return F
def Kelvin(K):
    K = float(input("Masukkan besar suhu dalam kelvin: "))
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    print("Celcius\t\t:", str(float(K-273.15))+"° Kelvin")
    print("Fahrenheit\t:", str(float((9/5)*(K-273.15)+32))+"° Fahrenheit")
    print("Reamur\t\t:", str(float((4/5)*(K-273.15)))+"° Reamur")
    return K
def Reamur(R):
    R = float(input("Masukkan besar suhu dalam reamur: "))
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    print("Celcius\t\t:", str(float(5/4)*R)+"° Celcius")
    print("Fahrenheit\t:", str(float((9/4)*R+32))+"° Fahrenheit")
    print("Kelvin\t\t:", str(float((5/4)*R+273.15))+"° Kelvin")
    return R

print("Hitungan konversi suhu")
jenis_suhu = ("1. Celcius", "2. Fahrenheit", "3. Kelvin", "4. Reamur")
for x,suhu in enumerate(jenis_suhu, start=1):
    print(suhu)

pilihan = int(input("\nPilih salah satu satuan yang akan diinput: "))
if pilihan == 1:
    Celcius('C')
elif pilihan ==2:
    Fahrenheit('F')
elif pilihan ==3:
    Kelvin('K')
elif pilihan ==4:
    Reamur('R')
else:
    print("Terjadi Error")
