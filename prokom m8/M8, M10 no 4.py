def Celcius():
    global Fahrenheit, Kelvin, Reamur
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    Fahrenheit = str(float((9/5)*C+32))+"° Fahrenheit"
    Kelvin = str(float(C+273.15))+"° Kelvin"
    Reamur = str(float((4/5)*C))+"° Reamur"
def Fahrenheit():
    global Celcius, Kelvin, Reamur
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    Celcius = str(float((5/9)*(F-32)))+"° Celcius"
    Kelvin = str(float((5/9)*(F-32)+273.15))+"° Kelvin"
    Reamur = str(float((4/9)*(F-32)))+"° Reamur"
def Kelvin():
    global Celcius, Fahrenheit, Reamur
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    Celcius = str(float(K-273.15))+"° Kelvin"
    Fahrenheit = str(float((9/5)*(K-273.15)+32))+"° Fahrenheit"
    Reamur = str(float((4/5)*(K-273.15)))+"° Reamur"
def Reamur():
    global Celcius, Fahrenheit, Kelvin
    print("Apabila dikonversi ke satuan suhu lain menjadi: ")
    Celcius = str(float((5/4)*R))+"° Celcius"
    Fahrenheit = str(float((9/4)*R+32))+"° Fahrenheit"
    Kelvin = str(float((5/4)*R+273.15))+"° Kelvin"

print("Hitungan konversi suhu")
jenis_suhu = ("1. Celcius", "2. Fahrenheit", "3. Kelvin", "4. Reamur")
for x,suhu in enumerate(jenis_suhu, start=1):
    print(suhu)

pilihan = int(input("\nPilih salah satu satuan yang akan diinput: "))
if pilihan == 1:
    C = float(input("Masukkan besar suhu 'Celcius' : "))
    Celcius()
    print("Fahrenheit\t: ", Fahrenheit)
    print("Kelvin\t\t: ", Kelvin)
    print("Reamur\t\t: ", Reamur)
elif pilihan ==2:
    F = float(input("Masukkan besar suhu dalam 'Fahrenheit' : "))
    Fahrenheit()
    print("Celcius\t\t:", Celcius)
    print("Kelvin\t\t:", Kelvin)
    print("Reamur\t\t:", Reamur)
elif pilihan ==3:
    K = float(input("Masukkan besar suhu dalam 'Kelvin' : "))
    Kelvin()
    print("Celcius\t\t:", Celcius)
    print("Fahrenheit\t:", Fahrenheit)
    print("Reamur\t\t:", Reamur)
elif pilihan ==4:
    R = float(input("Masukkan besar suhu dalam 'Reamur' : "))
    Reamur()
    print("Celcius\t\t:", Celcius)
    print("Fahrenheit\t:", Fahrenheit)
    print("Kelvin\t\t:", Kelvin)
else:
    print("Terjadi Error")
